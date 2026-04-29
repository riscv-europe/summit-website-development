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
import json
import os
import sys
import logging
from datetime import datetime
import csv
from typing import Dict, List, Iterator, Any

try:
    import requests
except ImportError:
    print("ERROR: This script requires the 'requests' library.", file=sys.stderr)
    print("Install it with: pip install requests", file=sys.stderr)
    sys.exit(1)


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
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
# API Helper Functions (inlined for standalone operation)
# ============================================================================

def make_api_session(api_key: str) -> requests.Session:
    """
    Create a requests session with authentication for Pretalx API.

    Args:
        api_key: Pretalx API key

    Returns:
        Configured requests session
    """
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Token {api_key}",
        "Content-Type": "application/json",
    })
    return session


def api_get(session: requests.Session, url: str, params: Dict = None) -> Dict:
    """
    Make a GET request to the API and return JSON response.

    Args:
        session: Requests session with auth configured
        url: Full API URL
        params: Optional query parameters

    Returns:
        JSON response as dict

    Raises:
        requests.HTTPError: If request fails
    """
    response = session.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def paginate(session: requests.Session, url: str, params: Dict = None,
             result_key: str = "results") -> Iterator[Dict]:
    """
    Paginate through API results.

    Args:
        session: Requests session with auth configured
        url: Base API URL
        params: Optional query parameters
        result_key: Key in response containing results list

    Yields:
        Individual items from paginated results
    """
    params = params.copy() if params is not None else {}
    page = 1
    fetched_count = 0

    while True:
        params["page"] = page
        data = api_get(session, url, params)

        results = data.get(result_key, [])
        if not results:
            break

        fetched_count += len(results)
        total = data.get("count", fetched_count)
        log.info(f"  [{result_key}] page {page} -- {fetched_count}/{total}")

        for item in results:
            yield item

        # Check if there are more pages
        if not data.get("next"):
            break

        page += 1


# ============================================================================
# Submission Export Functions
# ============================================================================

def fetch_speakers(session: requests.Session, base_url: str) -> Dict[str, List[Dict]]:
    """
    Fetch all speakers from Pretalx API.

    Args:
        session: Authenticated requests session
        base_url: Base API URL (e.g., https://cfp.../api/events/xxx/)

    Returns:
        Dict mapping submission_code to list of speakers:
        {submission_code: [{"name": str, "email": str}, ...]}
    """
    speakers_url = f"{base_url}speakers/"

    log.info("Fetching speakers from Pretalx API...")
    speakers = list(paginate(session, speakers_url, {}))  # Uses default result_key="results"
    log.info(f"Fetched {len(speakers)} speakers")

    # Map speakers to submissions
    speaker_map = {}
    for sp in speakers:
        name = (sp.get("name") or "").strip()
        email = (sp.get("email") or "").strip()

        for sub_code in (sp.get("submissions") or []):
            if sub_code not in speaker_map:
                speaker_map[sub_code] = []
            speaker_map[sub_code].append({
                "name": name,
                "email": email,
            })

    return speaker_map


def get_pdf_url_from_answers(answers: List[Dict], track_id: int) -> str:
    """
    Extract PDF URL from submission answers based on track.

    Args:
        answers: List of answer objects from submission
        track_id: Track ID (4=blind, 5=non-blind, 6=demo)

    Returns:
        PDF URL string or empty string if not found
    """
    # Determine which question ID to look for based on track
    if track_id == 4:  # blind
        target_q = Q_BLIND_PDF
    elif track_id == 5:  # non-blind
        target_q = Q_NONBLIND_PDF
    elif track_id == 6:  # demo
        target_q = Q_DEMO_PDF
    else:
        return ""

    for ans in answers:
        if ans.get("question") == target_q:
            return ans.get("answer_file") or ""

    return ""


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

    for sub in submissions:
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
        speaker_names = [s["name"] for s in speakers if s["name"]]

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
        "-d", "--output-dir",
        default= f"_data/summit{summitYear}",
        help= f"Root dir for all CSV output files (defaults to \"_data/summit{summitYear}\")"
    )
    parser.add_argument(
        "-p", "--posters",
        default="posters.csv",
        help="CSV output file for posters (defaults to \"posters.csv\")"
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

    args = parser.parse_args()

    # Configure logging level
    if args.verbose:
        log.setLevel(logging.DEBUG)
    elif args.quiet:
        log.setLevel(logging.WARNING)

    # Get API credentials from environment
    api_key = os.getenv("PRETALX_API_KEY")
    api_url = os.getenv("PRETALX_API_URL")

    if not api_key or not api_url:
        log.error("ERROR: PRETALX_API_KEY and PRETALX_API_URL must be set")
        log.error("Example:")
        log.error('  export PRETALX_API_KEY="your-api-key"')
        log.error('  export PRETALX_API_URL="https://cfp.example.com/api/events/your-event/"')
        sys.exit(1)

    # Ensure URL ends with /
    if not api_url.endswith("/"):
        api_url += "/"

    # Create API session
    log.info("Creating API session...")
    session = make_api_session(api_key)

    try:
        # Fetch speakers first
        speaker_map = fetch_speakers(session, api_url)

        # Fetch submissions
        log.info("Fetching and processing submissions...")
        submissions = fetch_submissions(session, api_url, speaker_map)

        # Sort by track and then by ID for consistent ordering
        submissions.sort(key=lambda x: (x.get("track", ""), x.get("id", "")))

        # Compute the full relative path name of the posters CSV file.
        posters_csv = f"{args.output_dir}{posters}" if args.output_dir[:-1] == '/' else f"{args.output_dir}/{args.posters}"

        # Write to CSV file
        log.info(f"Writing {len(submissions)} submissions to {posters_csv}...")

        with open(posters_csv, mode='w') as csv_file:
            # Collect the columns names.
            headers = submissions[0].keys() if submissions else []

            # Create a DictWriter object
            writer = csv.DictWriter(csv_file, fieldnames=headers, lineterminator="\n")

            # Write the header.
            writer.writeheader()

            # Write submisions
            for sub in submissions:
                writer.writerow(sub)

        log.info(f"Export complete: {posters_csv}")

        # Print summary
        type_counts = {}
        track_counts = {}
        for sub in submissions:
            sub_type = sub["type"]
            track = sub["track"]
            type_counts[sub_type] = type_counts.get(sub_type, 0) + 1
            track_counts[track] = track_counts.get(track, 0) + 1

        print()
        print("=" * 60)
        print("EXPORT SUMMARY")
        print("=" * 60)
        print(f"Total submissions: {len(submissions)}")
        print()
        print("By type:")
        for sub_type, count in sorted(type_counts.items()):
            print(f"  {sub_type:20} {count:3}")
        print()
        print("By track:")
        for track, count in sorted(track_counts.items()):
            print(f"  {track:20} {count:3}")
        print()
        print(f"Output file: {posters_csv}")
        print("=" * 60)

    except requests.HTTPError as e:
        log.error(f"HTTP Error: {e}")
        log.error(f"Response: {e.response.text if hasattr(e, 'response') else 'N/A'}")
        sys.exit(1)
    except Exception as e:
        log.error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
