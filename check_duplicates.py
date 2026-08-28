#!/usr/bin/env python3
"""Fail if acronyms.csv contains duplicate (Acronym, Meaning) entries.

An acronym is allowed to appear more than once as long as each row has a
different Meaning (e.g. "IP" = Intellectual Property vs. Internet Protocol).
Two rows are considered duplicates when the Acronym and Meaning match after
trimming whitespace and normalizing case, even if Context/Notes differ.
"""
import csv
import sys
from collections import defaultdict


def find_duplicates(csv_file):
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows_by_key = defaultdict(list)
        for line_number, row in enumerate(reader, start=2):  # header is line 1
            acronym = (row.get("Acronym") or "").strip().casefold()
            meaning = (row.get("Meaning") or "").strip().casefold()
            rows_by_key[(acronym, meaning)].append(
                (line_number, row.get("Acronym", ""), row.get("Meaning", ""))
            )

    return {key: entries for key, entries in rows_by_key.items() if len(entries) > 1}


def main(argv):
    csv_file = argv[1] if len(argv) > 1 else "acronyms.csv"
    duplicates = find_duplicates(csv_file)

    if not duplicates:
        return 0

    print(f"Found {len(duplicates)} duplicate acronym/meaning pair(s) in {csv_file}:\n")
    for (_, _), entries in duplicates.items():
        acronym, meaning = entries[0][1], entries[0][2]
        lines = ", ".join(f"line {ln}" for ln, _, _ in entries)
        print(f"  {acronym} - {meaning.strip()} ({lines})")

    print("\nRemove or consolidate the duplicate row(s) above before committing.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
