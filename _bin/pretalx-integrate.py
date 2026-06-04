#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""
pretalix-import.py — Export submission data for website.

Exports submission information including speakers for all tracks
(blind, non-blind, demos, etc.) in a standalone script with no
external dependencies.

This script is READ-ONLY and only makes GET requests to the Pretalx
API.

Usage:
    export PRETALX_API_KEY="your-api-key"
    export PRETALX_API_URL="https://cfp.example.com/api/events/your-event/"
    python3 pretalix-import.py [--output FILE] [--pretty]

First version by Nick.  Updated and fine-tuned to fit the web site
production process by Christian.

"""

import argparse
import pprint
import json
import os
import sys
import logging
import traceback
from datetime import datetime
import csv
from typing import Dict, List, Iterator, Any

try:
    import requests
except ImportError:
    print("ERROR: This script requires the 'requests' library.", file=sys.stderr)
    print("Install it with: pip install requests", file=sys.stderr)
    sys.exit(1)

def __FILE__():
    stack = traceback.extract_stack()
    return stack[-2].filename

def __LINE__():
    stack = traceback.extract_stack()
    return stack[-2].lineno

# Drop print(f"At: {__FILE__()}:{__LINE__()}") wherever you want in
# the code for quick-and-dirty, C style, old fashioned debug.

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='../pretalx-integrate.log'
)
log = logging.getLogger(__name__)


# Track definitions
TRACKS = {
    4: "blind",
    5: "non-blind",
    6: "demo",
}

# Question IDs for PDF URLs
Q_BLIND_PDF = 2
Q_NONBLIND_PDF = 3
Q_DEMO_PDF = 4




# ============================================================================
# Old code from the query oriented script. Kept as reference.
# ============================================================================


def fetch_submissions(session: requests.Session, base_url: str,
                     speaker_map: Dict[str, List[Dict]]) -> List[Dict]:
    """
    Fetch all submissions with expanded data.

    Args:
        session: Authenticated requests session
        base_url: Base API URL
        speaker_map: Dict mapping submission codes to speakers

    Returns:
        List of submission dicts ready for JSON export
    """
    submissions_url = f"{base_url}submissions/"
    params = {
        "expand": "answers,submission_type",  # Expand answers and submission type
    }

    log.info("Fetching submissions from Pretalx API...")
    submissions = list(paginate(session, submissions_url, params))  # Uses default result_key="results"
    log.info(f"Fetched {len(submissions)} submissions")

    # Process submissions for export (only accepted/confirmed)
    export_data = []
    skipped_count = 0

    for index,sub in enumerate(submissions):
        # The counter 'index' is not used in the production code below
        # when the dataset is sane. But might comme it handy when the
        # dataset has inconsitencies and debug is required.
        code = sub.get("code")
        if not code:
            continue

        # Only export accepted or confirmed submissions
        state = sub.get("state")
        if state not in ["accepted", "confirmed"]:
            skipped_count += 1
            continue

        # Get track (blind/non-blind/demo)
        track_id = sub.get("track")
        track_name = TRACKS.get(track_id, f"unknown-{track_id}")

        # Get submission type (talk/poster)
        submission_type = sub.get("submission_type")
        if isinstance(submission_type, dict):
            # Could be nested like {'en': 'Talk'} or have a 'name' field
            type_name = submission_type.get("en") or submission_type.get("name", "")
            if isinstance(type_name, dict):
                type_name = type_name.get("en", "")
        else:
            type_name = str(submission_type) if submission_type else "unknown"

        # Get PDF URL from answers
        answers = sub.get("answers", [])
        pdf_url = get_pdf_url_from_answers(answers, track_id)

        # Get abstract from answers
        abstract = sub.get("abstract", [])

        # Get speakers for this submission
        speakers = speaker_map.get(code, [])
        # Some papers are written by ghosts.
        speaker_names = "(null)" if speakers == [] else [s["name"] for s in speakers if s["name"]]

        # Build export record
        record = {
            "Id": code,
            "Title": sub.get("title", ""),
            "Type": type_name.lower() if type_name else "unknown",
            "track": track_name,
            "abstract_url": pdf_url,
            # "Authors": speaker_names,
            "Authors": speaker_names[0] if len(speaker_names) <= 1 else ", ".join(speaker_names[:-1]) + " and " + speaker_names[-1],
            "Abstract": abstract,
        }

        export_data.append(record)

    log.info(f"Filtered to {len(export_data)} accepted/confirmed submissions (skipped {skipped_count} in other states)")

    return export_data

import json

def read_schedule_json_db(json_file_path):
    """
    Read a JSON shedule

    Args:
        json_file_path (str): path to the JSON file.

    Returns:
        list: list of dict, representing the JSON file content.
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # If the JSON file was a listy of objects.
            if isinstance(data, list):
                return data
            # If the JSON file was a single object.
            elif isinstance(data, dict):
                return [data]
            else:
                raise ValueError("The JSON file does not a single object nor a list of objects.")

    except FileNotFoundError:
        print(f"Error: file '{json_file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: file {json_file_path} is not a valid JSON file.")
        return []
    except Exception as e:
        print(f"Error: unexpected error {e} occured")
        return []


# The list of poster islands, build while parsing the database.
islands = []

# ============================================================================
# Main
# ============================================================================

def main():
    """Main entry point."""

    # We assume that after August, we're talking about the Summit of
    # next year.
    year  = datetime.now().year
    month = datetime.now().month
    summitYear = year+1 if month > 8 else year

    parser = argparse.ArgumentParser(
        description="Export submission data for website in CSV format (READ-ONLY)"
    )
    parser.add_argument(
        "-o", "--output-dir",
        default = f"_data/summit{summitYear}/integrated",
        help= "Root dir for all CSV output files. Defaults to \"%(default)s\"."
    )
    parser.add_argument(
        "-p", "--posters",
        default="posters.csv",
        help="CSV output file for posters. Defaults to \"%(default)s\"."
    )
    parser.add_argument(
        "-t", "--talks",
        default="talks.csv",
        help="CSV output file for talks. Defaults to \"%(default)s\"."
    )
    parser.add_argument(
        "-d", "--demos",
        default="demos.csv",
        help="CSV output file for academic demos. Defaults to \"%(default)s\"."
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON with indentation."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose debug logging."
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress informational messages."
    )

    parser.add_argument(
        "schedule.json",
        help="the pretalx schedule dump as a single JSON file",
        default="../schedule.json"
    )

    # Parse CLI arguments. Note that postional arguments with a '.'
    # require some hackery.
    args = parser.parse_args()
    args_schedule_json = vars(args)['schedule.json']
    
    # Configure logging level
    if args.verbose:
        log.setLevel(logging.DEBUG)
    elif args.quiet:
        log.setLevel(logging.WARNING)

    # Auxiliary conversion of days to a shorthand
    def filter_day(perf):
        day = perf["Start (date)"]
        if   day == "2026-06-09":
            return "09-Tue"
        elif day == "2026-06-10":
            return "10-Wed"
        elif day == "2026-06-11":
            return "11-Thu"
        else:
            log.warning(f"Unknown day for perf {perf['ID']}: '{day}'.")
            return "(day?)"

    # Auxiliary conversion of time to 5 chars.
    def filter_time(perf):
        time = perf["Start (time)"]
        return time[0:5].replace(':','h')

    # Auxiliary filter of blindness submission status.
    def filter_blindness(perf):
        blindness = perf ["Track"]["en"]
        if   blindness == "Blind Submission (Default)":
            return "Blind"
        elif blindness == "Non-Blind submission":
            return "Non-blind"
        else:
            log.warning(f"Unknown blindness for perf {perf['ID']}: '{blindness}'.")
            return False

    # Auxiliary formating of authors, from a table to a string
    def format_authors(authors):
        if len(authors) <= 2:
            return " and ".join(authors)
        else:
            return f"{', '.join(authors[:-1])}, and {authors[-1]}"

    # Auxiliary CSV writer of a given kind of performance.
    def write_performances_to_CSV_file(perfs, csv_file_name):
        csv_file_path = f"{args.output_dir}{csv_file_name}" if args.output_dir[:-1] == '/' else f"{args.output_dir}/{csv_file_name}"

        log.info(f"{csv_file_path}: start writing...")

        if len(perfs) > 0:
            with open(csv_file_path, mode='w') as csv_file:
                # Collect the columns names.
                headers = perfs[0].keys()

                # Create a DictWriter object
                writer = csv.DictWriter(csv_file, fieldnames=headers, lineterminator="\n")

                # Write the header.
                writer.writeheader()

                # Write submisions
                for perf in perfs:
                    writer.writerow(perf)

        log.info(f"{csv_file_path}: wrote {len(perfs)} entries.")

    # Auxliary function to stream line and accumulate poster islands
    # names.
    def reformat_and_accumulate_island(perf):
        # Islands are named like "Poster Island A". We just keep the "A".
        island = str(perf["Room"]["en"][-1])
        if island not in islands:
            islands.append(island)
        return island

    # Auxiliary function to make the difference bewteeen keynotes
    # (boths sponsors and invited) and invited talks.
    def is_a_keynote(perf):
        if perf["Track"]["en"] == "Keynotes":
            return True
        else:
            return False

    try:
        # Let's call 'performances' all the various kind of talks,
        # demo, etc.
        performances = read_schedule_json_db(args_schedule_json)

        posters = []
        talks = []
        keynotes = []
        demos = []
        invited_talks = []
        demo_theaters = []
        for perf in performances:
            if (perf["Proposal state"] == "rejected" or
                perf["Proposal state"] == "withdrawn" or
                perf["Proposal state"] == "canceled"):
                continue

            # We take the last word of the first speaker full name as
            # the last name for file name (quite some names, isnt'it).
            last_name_for_file_name = perf['Speaker names'][0].split()[-1].upper() if perf['Speaker names'] else "NONAME"

            base_file_name = f"{perf['Start (date)']}-RISC-V-Summit-Europe-{filter_time(perf)}-{last_name_for_file_name}"

            session_type = perf["Session type"]["en"]
            if session_type == "Poster":
                posters = posters + [{
                    "Id": perf["ID"],
                    "Type": "poster",
                    "Island": reformat_and_accumulate_island(perf),
                    "track": "",
                    "Day": filter_day(perf),
                    "Blindness": filter_blindness(perf),
                    "AbstractFileName": f"{base_file_name}-abstract.pdf",
                    "PosterFileName": f"{base_file_name}-poster.pdf",
                    "Title": perf["Proposal title"],
                    "Authors": format_authors(perf["Speaker names"]),
                    "Abstract": perf["Abstract"],
                }]
            elif session_type == "Talk":
                talks = talks + [{
                    "Id": perf["ID"],
                    "Type": "talk",
                    "Blindness": filter_blindness(perf),
                    "Day": filter_day(perf),
                    "Time": filter_time(perf),
                    "AbstractFileName": f"{base_file_name}-abstract.pdf",
                    "SlidesFileName": f"{base_file_name}-slides.pdf",
                    "Title": perf["Proposal title"],
                    "Authors": format_authors(perf["Speaker names"]),
                    "abstract_url": "",
                    "Abstract": perf["Abstract"],
                }]
            elif session_type == "Invited talk":
                if is_a_keynote(perf):
                    keynotes = keynotes + [{
                        "Id": perf["ID"],
                        "Type": "keynote",
                        "Day": filter_day(perf),
                        "Time": filter_time(perf),
                        "AbstractFileName": f"{base_file_name}-abstract.pdf",
                        "SlidesFileName": f"{base_file_name}-slides.pdf",
                        "Title": perf["Proposal title"],
                        "Authors": format_authors(perf["Speaker names"]),
                        "abstract_url": "",
                        "Abstract": perf["Abstract"],
                    }]
                else:
                    invited_talks = invited_talks + [{
                        "Id": perf["ID"],
                        "Type": "invited talk",
                        "Blindness": filter_blindness(perf),
                        "Day": filter_day(perf),
                        "Time": filter_time(perf),
                        "AbstractFileName": f"{base_file_name}-abstract.pdf",
                        "SlidesFileName": f"{base_file_name}-slides.pdf",
                        "Title": perf["Proposal title"],
                        "Authors": format_authors(perf["Speaker names"]),
                        "abstract_url": "",
                        "Abstract": perf["Abstract"],
                    }]
            elif session_type == "Demo":
                demos = demos + [{
                    "Id": perf["ID"],
                    "Type": "demo",
                    "Day": filter_day(perf),
                    "Time": filter_time(perf),
                    "AbstractFileName": f"{base_file_name}-abstract.pdf",
                    "Title": perf["Proposal title"],
                    "Authors": format_authors(perf["Speaker names"]),
                    "abstract_url": "",
                    "Abstract": perf["Abstract"],
                }]
            elif session_type == "Demo Theater presentation":
                demo_theaters = demo_theaters + [{
                    "Id": perf["ID"],
                    "Title": perf["Proposal title"],
                    "Type": "demo_theater",
                    "Authors": format_authors(perf["Speaker names"]),
                    "Abstract": perf["Abstract"],
                    "Day": filter_day(perf),
                }]
            else:
                log.warning(f"Unknown session type: {repr(session_type)}.")

        # We fold talks and keynotes into a single table.
        presentations = talks + keynotes + invited_talks

        print(f"Talks: {len(talks)}")
        print(f"Keynotes: {len(keynotes)}")
        print(f"Invited talks: {len(invited_talks)}")
        print(f"Presentations (keynotes+talks+invited_talks): {len(presentations)}")
        print(f"Posters: {len(posters)}")
        print(f"Demos: {len(demos)}")
        print(f"Demo theater pres: {len(demo_theaters)}")

        write_performances_to_CSV_file(posters,args.posters)
        write_performances_to_CSV_file(demos,args.demos)
        write_performances_to_CSV_file(presentations,"presentations.csv")

    except requests.HTTPError as e:
        log.error(f"HTTP Error: {e}")
        log.error(f"Response: {e.response.text if hasattr(e, 'response') else 'N/A'}")
        sys.exit(1)
    except Exception as e:
        log.error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
