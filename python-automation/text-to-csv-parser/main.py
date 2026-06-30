#!/usr/bin/env python3
"""
Structured Text to CSV Parser

Converts semi-structured text records into a clean CSV file.

Example input block:

customer_id: CUST-001
email: customer@example.com
status: active

Output columns:

customer_id,email,status
"""

import argparse
import csv
import re
import sys
from pathlib import Path


FIELD_NAMES = ["customer_id", "email", "status"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert semi-structured text records into CSV."
    )

    parser.add_argument(
        "-i",
        "--input",
        default="input.txt",
        help="Path to the input TXT file. Default: input.txt",
    )

    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Path to the output CSV file. Default: same name as input with .csv extension",
    )

    parser.add_argument(
        "--skip-incomplete",
        action="store_true",
        help="Skip records with missing fields instead of writing empty cells.",
    )

    return parser.parse_args()


def read_text_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError as error:
        print(f"Error reading input file: {error}", file=sys.stderr)
        sys.exit(1)


def split_records(text: str) -> list[str]:
    return [block.strip() for block in re.split(r"\n\s*\n", text.strip()) if block.strip()]


def extract_field(record: str, field_name: str) -> str:
    pattern = rf"^{field_name}\s*:\s*(.+)$"
    match = re.search(pattern, record, re.IGNORECASE | re.MULTILINE)
    return match.group(1).strip() if match else ""


def parse_record(record: str) -> dict[str, str]:
    return {field: extract_field(record, field) for field in FIELD_NAMES}


def is_complete(record: dict[str, str]) -> bool:
    return all(record.values())


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    try:
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
            writer.writeheader()
            writer.writerows(rows)
    except OSError as error:
        print(f"Error writing output file: {error}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    args = parse_args()

    input_path = Path(args.input)

    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    output_path = Path(args.output) if args.output else input_path.with_suffix(".csv")

    text = read_text_file(input_path)
    raw_records = split_records(text)

    parsed_rows = []
    incomplete_count = 0

    for record in raw_records:
        parsed_record = parse_record(record)

        if not any(parsed_record.values()):
            continue

        if not is_complete(parsed_record):
            incomplete_count += 1

            if args.skip_incomplete:
                continue

        parsed_rows.append(parsed_record)

    write_csv(output_path, parsed_rows)

    print("Processing completed.")
    print(f"Records processed: {len(raw_records)}")
    print(f"Rows written: {len(parsed_rows)}")
    print(f"Incomplete records: {incomplete_count}")
    print(f"Output file: {output_path}")


if __name__ == "__main__":
    main()
