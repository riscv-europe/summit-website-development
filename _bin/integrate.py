#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This python script consolidates information from various CSV files
   to ease Summit web site generation."""
import csv
import argparse
import sys
import os
import shutil

args = {}

posters_agenda_csv = "posters-agenda.csv"

full_days = {
    "Tue": "2025-05-13",
    "Wed": "2025-05-14",
    "Thu": "2025-05-15"
}

def read_csv(filename):
    """Read a CSV file and return its contents as a list of rows."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)
            return data
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"Error reading {filename}: {str(e)}")
        return None

def ensure_column(rows, column):
    """Make sure that each row has this column."""
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Each row must be a dictionary")
        if column not in row:
            row[column] = None

def create_posters_PDFs_filenames(posters, subs):
    """Create the filenames for posters and their abstracts"""
    reverse_subs = {}
    for sub in subs:
        reverse_subs[sub['Submission ID']] = sub
    for poster in posters:
        if poster['PosterId'] != "":
            sub = reverse_subs[poster['PosterId']]
            full_day = full_days[poster['Day']]
            island = poster['Island']
            stand = poster['StantRank'] # The T in StantRank is an unfortunate typo, here to stay.
            first_name = sub['1: First Name'].strip().title()
            last_name  = sub['1: Last Name' ].strip().upper().replace(" ","-")
            poster['AbstractPDFFileName'] = f"{full_day}-RISC-V-Summit-Europe-P{island}.{stand}-{last_name}-abstract.pdf"
            poster['PosterPDFFileName'  ] = f"{full_day}-RISC-V-Summit-Europe-P{island}.{stand}-{last_name}-poster.pdf"
            poster['FirstAuthorName'    ] = f"{first_name} {last_name}"

def check_and_import_posters(posters, src_dir, dest_dir):
    for poster in posters:
        poster_id = poster['PosterId']
        if poster_id == "": # Some poster stands may be empty.
            continue
        poster_dir = os.path.join(src_dir,poster_id)
        abstract_found = False
        poster_found = False
        if os.path.exists(poster_dir):
            for file in os.listdir(poster_dir):
                abstract_file = f"{poster_id}_Abstract.pdf"
                poster_file   = f"{poster_id}_Poster.pdf"
                if file == abstract_file:
                    src_path  = os.path.join(src_dir,poster_id,abstract_file)
                    dest_path = os.path.join(dest_dir,poster['AbstractPDFFileName'])
                    if os.path.exists(src_path):
                        shutil.copy(src_path,dest_path)
                        abstract_found = True
                    else:
                        print(f"No file: {src_path}")
                elif file == poster_file:
                    src_path  = os.path.join(src_dir,poster_id,poster_file)
                    dest_path = os.path.join(dest_dir,poster['PosterPDFFileName'])
                    if os.path.exists(src_path):
                        shutil.copy(src_path,dest_path)
                        poster_found = True
                    else:
                        print(f"No file: {src_path}")
                else:
                    print(f"Poster {poster_id:>3} has unused file '{file}' ({poster['FirstAuthorName']}).", file=sys.stderr)
        if abstract_found == False:
            print(f"Poster {poster_id:>3} has no abstract ({poster['FirstAuthorName']}).", file=sys.stderr)
            poster['AbstractPDFFileName'] = None
        if poster_found == False:
            print(f"Poster {poster_id:>3} has no poster ({poster['FirstAuthorName']}).", file=sys.stderr)
            poster['PosterPDFFileName'] = None

def main():
    """Consolidate information from CSV files before using them to generate the web site."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Read two CSV files")
    parser.add_argument('--agenda',      required=True,  help="Path to the summit's agenda CSV file")
    parser.add_argument('--posters',     required=True,  help="Path to the posters' CSV file")
    parser.add_argument('--subm',        required=True,  help="Path to the submitted talks/posters' CSV file")
    parser.add_argument('--invited',     required=True,  help="Path to the invited talks' CSV file")
    parser.add_argument('--submitted-pdfs', required=False, help="Path to the submitted PDFs source dir", default=".")
    parser.add_argument('--published-pdfs', required=False, help="Path to the published PDFs target dir", default=".")
    parser.add_argument('--integrated-csvs',required=True,  help="Path for the integrated generated CSV files")
    parser.add_argument('--debug',       required=False, help="Dump the input file contents for debug purposes.", action="store_true", default=False)

    # Parse arguments
    global args
    args = parser.parse_args()
    
    # Read the files
    agenda      = read_csv(args.agenda)
    posters     = read_csv(args.posters)
    subm        = read_csv(args.subm)
    invited     = read_csv(args.invited)

    # Check if files were read successfully
    if agenda is None or posters is None or subm is None or invited is None:
        print("Cannot proceed due to file reading errors.")
        sys.exit(1)

    # Somme bookeeping to prepare posters' table for further
    # processing: (1) Ensure that there are columns for posters'
    # abstract and actual poster filenames. (2) Create the actual
    # files names for posters' abstract and actual poster. (3) filter
    # out empty poster slots. (4) Sort by PosterId to ease reporting
    # of missing PDF files on stderr.
    ensure_column(posters,'AbstractPDFFileName')
    ensure_column(posters,'PosterPDFFileName')
    ensure_column(posters,'FirstAuthorName')
    posters = [poster for poster in posters if poster['PosterId'] != ""]
    posters = sorted(posters, key=lambda poster: int(poster['PosterId']))
    create_posters_PDFs_filenames(posters,subm)


    # If debug is on, display the contents of the input files.
    if args.debug:
        print(f"\nContents of {args.posters}, with extra fields:")
        for poster in posters:
            print(poster)

    # Check and import posters' asbtract and actual poster files.
    check_and_import_posters(posters,args.submitted_pdfs,args.published_pdfs)

    # Prepate posters for final publishing on the web site: (1) remove
    # the field of the 1st author's name; (2) sort posters ordering
    # back to (day, island, stand).
    for poster in posters:
        del poster['FirstAuthorName']
    def poster_ordering(poster):
        sorted_days = {
            "Tue": 1,
            "Wed": 2,
            "Thu": 3,
        }
        return (sorted_days.get(sorted_days.get(poster['Day'])),poster['Island'],poster['StantRank']) # 'Stant' is an unfortunate typo. Should be 'Stand'.
    posters.sort(key=poster_ordering)

    # Write to posters' agenda file.
    os.makedirs(args.integrated_csvs, exist_ok=True)
    posters_agenda = os.path.join(args.integrated_csvs,posters_agenda_csv)
    with open(posters_agenda, mode="w", newline='') as file:
        header = posters[0].keys()
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(posters)
    print(f"Posters, islands and stands described in '{posters_agenda}'.")

if __name__ == "__main__":
    main()
