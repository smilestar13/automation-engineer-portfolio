# Text to CSV Parser

## Overview

This utility converts semi-structured text records into a structured CSV file suitable for automation workflows, reporting, and data migration.

The parser extracts predefined fields from text blocks and exports them into a clean tabular format while preserving incomplete records or optionally skipping them.

The project demonstrates practical Python techniques commonly used in business automation and ETL pipelines.

---

## Business Scenario

Many internal systems export information as plain text instead of structured datasets.

Before this information can be imported into spreadsheets, databases, or automation platforms, it must first be normalized into a machine-readable format.

This utility automates that transformation.

Typical use cases include:

- Legacy system exports
- Log processing
- Data migration
- ETL pipelines
- Automation workflows
- Spreadsheet preparation

---

## Example Input

```text
customer_id: CUST-001
email: john.smith@example.com
status: active

customer_id: CUST-002
email: emily.johnson@example.com
status: pending
```

---

## Example Output

```csv
customer_id,email,status
CUST-001,john.smith@example.com,active
CUST-002,emily.johnson@example.com,pending
```

---

## Features

- Parse semi-structured text records
- Convert data into CSV format
- Automatic field extraction
- Missing field detection
- Optional skipping of incomplete records
- UTF-8 support
- Command-line interface
- Error handling
- Clean and reusable implementation

---

## Technologies

- Python 3
- argparse
- csv
- pathlib
- regular expressions (re)

---

## Repository Structure

```text
structured-text-to-csv-parser/

├── README.md
├── main.py
├── input.txt
└── input.csv
```

---

## Usage

Run using the default input file (`input.txt`):

```bash
python main.py
```

The generated output will automatically be saved as:

```text
input.csv
```

because the script uses the same filename as the input and only changes the extension.

---

Specify custom input and output files:

```bash
python main.py \
    --input records.txt \
    --output output.csv
```

---

Skip incomplete records:

```bash
python main.py \
    --input records.txt \
    --skip-incomplete
```

---

## Engineering Practices

This project demonstrates:

- Clean project organization
- Modular function design
- Command-line interfaces
- Input validation
- Exception handling
- Reusable parsing logic
- Maintainable Python code

---

## Notes

This repository contains demonstration data only.

All customer identifiers, email addresses, and records are fictional and have been created solely for demonstration purposes.

The parser is intended to illustrate a reusable data transformation workflow rather than process any real production data.

---

## Purpose

The goal of this project is to demonstrate how Python can be used to transform semi-structured text into structured datasets suitable for spreadsheets, databases, APIs, and automation platforms.
