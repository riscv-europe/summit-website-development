#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This python script consolidates information from various CSV files
   to ease Summit web site generation."""
import csv
import argparse
import sys

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

    # Parse arguments
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

    print(type(posters))
        
    # Make sure that each row has a column for posters's PDF.
    ensure_column(posters,'PosterPDF')
    
    # Display the contents of the files
    print(f"\nContents of {args.posters}:")
    for row in posters:
        print(row)
    
if __name__ == "__main__":
    main()
