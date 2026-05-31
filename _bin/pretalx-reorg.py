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
    filename='../pretalx-reorg.log'
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
        default= f"_data/summit{summitYear}",
        help= f"Root dir for all CSV output files (defaults to \"_data/summit{summitYear}\")"
    )
    parser.add_argument(
        "-p", "--posters",
        default="posters.csv",
        help="CSV output file for posters (defaults to \"posters.csv\")"
    )
    parser.add_argument(
        "-t", "--talks",
        default="talks.csv",
        help="CSV output file for talks (defaults to \"talks.csv\")"
    )
    parser.add_argument(
        "-d", "--demos",
        default="demos.csv",
        help="CSV output file for academic demos (defaults to \"demos.csv\")"
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON with indentation"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose debug logging"
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress informational messages"
    )

    parser.add_argument(
        "schedule.json",
        help="the pretalx's schedule dump as a single JSON file",
        default="../schedule.json",
    )


    # Parse CLI argguments. Note that postional arguments with a '.'
    # require some hackery.
    args = parser.parse_args()
    args_schedule_json = vars(args)['schedule.json']
    
    # Configure logging level
    if True or args.verbose:
        log.setLevel(logging.DEBUG)
    elif args.quiet:
        log.setLevel(logging.WARNING)

    # Filter days for a shorthand
    def filter_day(perf):
        day = perf["Start (date)"]
        if   day == "2026-06-09":
            return "09-Tue"
        elif day == "2026-06-10":
            return "10-Wed"
        elif day == "2026-06-11":
            return "11-Thu"
        else:
            log.warning(f"Unknown day: '{day}'.")
            return "(day?)"

    def filter_blindness(perf):
        blindness = perf ["Track"]["en"]
        if   blindness == "Blind Submission (Default)":
            return True
        elif blindness == "Non-Blind submission":
            return False
        else:
            log.warning(f"Unknown blindness: '{blindness}'.")
            return False

    try:
        # Let's call 'performances' all the various kind of talks,
        # demo, etc.
        performances = read_schedule_json_db(args_schedule_json)

        if performances:
            n = 2
            for i in range (n):
                print(f"Entry #{n}:")
                print(json.dumps(performances[i],indent=4, sort_keys=True))

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

            session_type = perf["Session type"]["en"]
            if session_type == "Poster":
                poster = {}
                poster["Id"] = perf["ID"]
                poster["Title"] = perf["Proposal title"]
                poster["Type"] = "poster"
                poster["track"] = ""
                poster["abstract_url"] = ""
                poster["Authors"] = perf["Speaker names"]
                poster["Abstract"] = perf["Abstract"]
                poster["Day"] = filter_day(perf)
                poster["Blind"] = filter_blindness(perf)
                posters = posters + [poster]
            elif session_type == "Talk":
                talk = {}
                talk["Id"] = perf["ID"]
                talk["Title"] = perf["Proposal title"]
                talk["Type"] = "talk"
                talk["track"] = ""
                talk["abstract_url"] = ""
                talk["Authors"] = perf["Speaker names"]
                talk["Abstract"] = perf["Abstract"]
                talk["Day"] = filter_day(perf)
                talk["Blind"] = filter_blindness(perf)
                talks = talks + [talk]
            elif session_type == "Keynotes":
                keynote = {}
                keynote["Id"] = perf["ID"]
                keynote["Title"] = perf["Proposal title"]
                keynote["Type"] = "keynote"
                keynote["abstract_url"] = ""
                keynote["Authors"] = perf["Speaker names"]
                keynote["Abstract"] = perf["Abstract"]
                keynote["Day"] = filter_day(perf)
                keynotes = keynotes + [keynote]
            elif session_type == "Demo":
                demo = {}
                demo["Id"] = perf["ID"]
                demo["Title"] = perf["Proposal title"]
                demo["Type"] = "demo"
                demo["abstract_url"] = ""
                demo["Authors"] = perf["Speaker names"]
                demo["Abstract"] = perf["Abstract"]
                demo["Day"] = filter_day(perf)
                demos = demos + [demo]
            elif session_type == "Invited talk":
                invited_talk = {}
                invited_talk["Id"] = perf["ID"]
                invited_talk["Title"] = perf["Proposal title"]
                invited_talk["Type"] = "invited_talk"
                invited_talk["abstract_url"] = ""
                invited_talk["Authors"] = perf["Speaker names"]
                invited_talk["Abstract"] = perf["Abstract"]
                invited_talk["Day"] = filter_day(perf)
                invited_talks = invited_talks + [invited_talk]
            elif session_type == "Demo Theater presentation":
                demo_theater = {}
                demo_theater["Id"] = perf["ID"]
                demo_theater["Title"] = perf["Proposal title"]
                demo_theater["Type"] = "demo_theater"
                demo_theater["Authors"] = perf["Speaker names"]
                demo_theater["Abstract"] = perf["Abstract"]
                demo_theater["Day"] = filter_day(perf)
                demo_theaters = demo_theaters + [demo_theater]
            else:
                log.warning(f"Unknown session type: {repr(session_type)}.")

        pprint.pprint(f"Nb posters: {len(posters)}")
        pprint.pprint(f"Nb talk: {len(talks)}")
        pprint.pprint(f"Nb keynotes: {len(keynotes)}")
        pprint.pprint(f"Nb demos: {len(demos)}")
        pprint.pprint(f"Nb invited talks: {len(invited_talks)}")
        pprint.pprint(f"Nb demo theater pres: {len(demo_theaters)}")

        # for i, row in enumerate(dict_table, 1):
        #     print(f"Ligne {i}: {row}")
        # submissions.sort(key=lambda x: (x.get("track", ""), x.get("id", "")))
        # Get only the posters.
        #        posters = [sub for sub in submissions if sub['Type'] == "poster"]

        # Compute the full relative path name of the posters CSV file.
        #posters_csv = f"{args.output_dir}{posters}" if args.output_dir[:-1] == '/' else f"{args.output_dir}/{args.posters}"

        # Write posters to CSV file
        # log.info(f"Writing {len(posters)} posters to {posters_csv}...")

        # with open(posters_csv, mode='w') as csv_file:
        #     # Collect the columns names.
        #     headers = posters[0].keys() if posters else []

        #     # Create a DictWriter object
        #     writer = csv.DictWriter(csv_file, fieldnames=headers, lineterminator="\n")

        #     # Write the header.
        #     writer.writeheader()

        #     # Write submisions
        #     for poster in posters:
        #         writer.writerow(poster)

        # log.info(f"Export complete: {posters_csv}")

        # # Get only the talks.
        # talks = [sub for sub in submissions if sub['Type'] == "talk"]

        # # Compute the full relative path name of the talks CSV file.
        # talks_csv = f"{args.output_dir}{talks}" if args.output_dir[:-1] == '/' else f"{args.output_dir}/{args.talks}"

        # # Write talks to CSV file
        # log.info(f"Writing {len(talks)} talks to {talks_csv}...")

        # with open(talks_csv, mode='w') as csv_file:
        #     # Collect the columns names.
        #     headers = talks[0].keys() if talks else []

        #     # Create a DictWriter object
        #     writer = csv.DictWriter(csv_file, fieldnames=headers, lineterminator="\n")

        #     # Write the header.
        #     writer.writeheader()

        #     # Write submisions
        #     for talk in talks:
        #         writer.writerow(talk)

        # log.info(f"Export complete: {talks_csv}")

        # # Get only the demos.
        # demos = [sub for sub in submissions if sub['Type'] == "demo"]

        # # Compute the full relative path name of the demos CSV file.
        # demos_csv = f"{args.output_dir}{demos}" if args.output_dir[:-1] == '/' else f"{args.output_dir}/{args.demos}"

        # # Write demos to CSV file
        # log.info(f"Writing {len(demos)} demos to {demos_csv}...")

        # with open(demos_csv, mode='w') as csv_file:
        #     # Collect the columns names.
        #     headers = demos[0].keys() if demos else []

        #     # Create a DictWriter object
        #     writer = csv.DictWriter(csv_file, fieldnames=headers, lineterminator="\n")

        #     # Write the header.
        #     writer.writeheader()

        #     # Write submisions
        #     for demo in demos:
        #         writer.writerow(demo)

        # log.info(f"Export complete: {demos_csv}")

        # # Print summary
        # type_counts = {}
        # track_counts = {}
        # for sub in submissions:
        #     sub_type = sub["Type"]
        #     track = sub["track"]
        #     type_counts[sub_type] = type_counts.get(sub_type, 0) + 1
        #     track_counts[track] = track_counts.get(track, 0) + 1

        # print()
        # print("=" * 60)
        # print("EXPORT SUMMARY")
        # print("=" * 60)
        # print(f"Total submissions: {len(submissions)}")
        # print()
        # print("By type:")
        # for sub_type, count in sorted(type_counts.items()):
        #     print(f"  {sub_type:20} {count:3}")
        # print()
        # print("By track:")
        # for track, count in sorted(track_counts.items()):
        #     print(f"  {track:20} {count:3}")
        # print()
        # print(f"Output file: {posters_csv}")
        # print("=" * 60)

    except requests.HTTPError as e:
        log.error(f"HTTP Error: {e}")
        log.error(f"Response: {e.response.text if hasattr(e, 'response') else 'N/A'}")
        sys.exit(1)
    except Exception as e:
        log.error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
