#!/usr/bin/env python3
"""
API Metrics Monitor

Reads resource identifiers from a text file, requests metric values from an
external API, and stores historical snapshots in a CSV report.

This script is designed as a reusable automation utility for monitoring
resource metrics over time.
"""

import argparse
import csv
import json
import random
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import requests


DEFAULT_API_URL = "https://api.example.com/v1/resources/metrics"
DEFAULT_INPUT_FILE = "identifiers.txt"
DEFAULT_OUTPUT_FILE = "resource_metrics.csv"
DEFAULT_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT = 15
DEFAULT_MIN_DELAY = 1.0
DEFAULT_MAX_DELAY = 3.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Monitor API metric values and store historical snapshots in CSV."
    )

    parser.add_argument(
        "-i",
        "--input",
        default=DEFAULT_INPUT_FILE,
        help=f"Input file with resource identifiers. Default: {DEFAULT_INPUT_FILE}",
    )

    parser.add_argument(
        "-o",
        "--output",
        default=DEFAULT_OUTPUT_FILE,
        help=f"Output CSV file. Default: {DEFAULT_OUTPUT_FILE}",
    )

    parser.add_argument(
        "--api-url",
        default=DEFAULT_API_URL,
        help="API endpoint URL.",
    )

    parser.add_argument(
        "--retry-attempts",
        type=int,
        default=DEFAULT_RETRY_ATTEMPTS,
        help=f"Number of retry attempts. Default: {DEFAULT_RETRY_ATTEMPTS}",
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"Request timeout in seconds. Default: {DEFAULT_TIMEOUT}",
    )

    parser.add_argument(
        "--min-delay",
        type=float,
        default=DEFAULT_MIN_DELAY,
        help=f"Minimum delay between requests in seconds. Default: {DEFAULT_MIN_DELAY}",
    )

    parser.add_argument(
        "--max-delay",
        type=float,
        default=DEFAULT_MAX_DELAY,
        help=f"Maximum delay between requests in seconds. Default: {DEFAULT_MAX_DELAY}",
    )

    return parser.parse_args()


def read_identifiers(path: Path) -> list[str]:
    if not path.exists():
        print(f"Input file not found: {path}", file=sys.stderr)
        sys.exit(1)

    identifiers = [
        line.strip()
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines()
        if line.strip()
    ]

    if not identifiers:
        print(f"No identifiers found in input file: {path}", file=sys.stderr)
        sys.exit(1)

    return identifiers


def read_existing_csv(path: Path) -> list[list[str]]:
    if not path.exists():
        return []

    with path.open("r", newline="", encoding="utf-8") as file:
        return list(csv.reader(file))


def write_csv(path: Path, rows: list[list[Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def parse_metric_value(response_data: dict[str, Any]) -> float | str:
    """
    Extract metric value from API response.

    Expected demo response format:

    {
        "result": {
            "data": {
                "metric_value": 123.45
            }
        }
    }
    """

    try:
        value = response_data["result"]["data"]["metric_value"]
        return round(float(value), 2)
    except (KeyError, TypeError, ValueError):
        return "ERROR"


def fetch_metric_value(
    resource_id: str,
    api_url: str,
    retry_attempts: int,
    timeout: int,
) -> float | str:
    payload = {
        "resource_id": resource_id,
    }

    for attempt in range(1, retry_attempts + 1):
        try:
            response = requests.get(
                api_url,
                params={"input": json.dumps(payload)},
                timeout=timeout,
            )
            response.raise_for_status()

            response_data = response.json()
            metric_value = parse_metric_value(response_data)

            if metric_value == "ERROR":
                raise ValueError("Metric value was not found in API response.")

            return metric_value

        except requests.RequestException as error:
            print(
                f"[ERROR] API request failed for {resource_id}. "
                f"Attempt {attempt}/{retry_attempts}: {error}"
            )

        except ValueError as error:
            print(
                f"[ERROR] Invalid API response for {resource_id}. "
                f"Attempt {attempt}/{retry_attempts}: {error}"
            )

        if attempt < retry_attempts:
            time.sleep(timeout)

    return "ERROR"


def is_number(value: Any) -> bool:
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False


def update_metrics_history(
    identifiers: list[str],
    output_path: Path,
    api_url: str,
    retry_attempts: int,
    timeout: int,
    min_delay: float,
    max_delay: float,
) -> None:
    existing_rows = read_existing_csv(output_path)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not existing_rows:
        headers = ["resource_id", timestamp]
        data_rows: dict[str, list[Any]] = {resource_id: [resource_id] for resource_id in identifiers}
    else:
        headers = existing_rows[0]
        data_rows = {row[0]: row for row in existing_rows[1:] if row}
        headers.append(timestamp)

    for resource_id in identifiers:
        print(f"[INFO] Processing resource: {resource_id}")

        metric_value = fetch_metric_value(
            resource_id=resource_id,
            api_url=api_url,
            retry_attempts=retry_attempts,
            timeout=timeout,
        )

        if resource_id not in data_rows:
            data_rows[resource_id] = [resource_id] + ["NULL"] * (len(headers) - 2)

        row = data_rows[resource_id]

        while len(row) < len(headers) - 1:
            row.append("NULL")

        previous_value = row[-1] if len(row) > 1 else None

        if is_number(metric_value):
            row.append(metric_value)
            print(f"[OK] {resource_id}: {metric_value}")
        else:
            row.append("ERROR")
            print(f"[WARN] {resource_id}: metric unavailable")

        if is_number(previous_value) and is_number(metric_value):
            delta = round(float(metric_value) - float(previous_value), 2)
            print(f"[INFO] Change since last snapshot: {delta}")

        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)

    updated_rows = [headers] + list(data_rows.values())
    write_csv(output_path, updated_rows)


def main() -> None:
    args = parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    identifiers = read_identifiers(input_path)

    update_metrics_history(
        identifiers=identifiers,
        output_path=output_path,
        api_url=args.api_url,
        retry_attempts=args.retry_attempts,
        timeout=args.timeout,
        min_delay=args.min_delay,
        max_delay=args.max_delay,
    )

    print(f"[DONE] Metrics report updated: {output_path}")


if __name__ == "__main__":
    main()
