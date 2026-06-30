# API Metrics Monitor

## Overview

API Metrics Monitor is a Python automation utility that retrieves metric values for multiple resources through a REST API and stores historical snapshots in a CSV report.

The project demonstrates a common enterprise automation pattern where external systems are queried periodically and their responses are recorded for reporting, monitoring, or further processing.

Rather than replacing previous results, every execution appends a new timestamped column, allowing historical values to be tracked over time.

---

## Business Scenario

Organizations often need to monitor hundreds or thousands of resources exposed through REST APIs.

Examples include:

- Internal services
- Servers
- Customer records
- Product catalogs
- External integrations
- Business objects

Instead of manually checking every resource, this utility automates the entire process by reading identifiers from a file, requesting data from an API, and maintaining a historical CSV report.

---

## Workflow Overview

```
Resource Identifiers
        │
        ▼
Read Input File
        │
        ▼
REST API Requests
        │
        ▼
Parse JSON Responses
        │
        ▼
Validate Results
        │
        ▼
Update Historical CSV
        │
        ▼
Generate Monitoring Report
```

---

## Features

- REST API integration
- JSON response parsing
- Automatic retry mechanism
- Timeout handling
- Randomized delay between requests
- Historical CSV snapshots
- Incremental report updates
- Command-line interface
- Local mock API support
- Production-style project structure

---

## Technologies

- Python 3
- Requests
- Flask
- CSV
- JSON
- argparse
- pathlib
- datetime

---

## Repository Structure

```
api-metrics-monitor/

├── README.md
├── main.py
├── mock_api.py
├── identifiers.txt
├── resource_metrics.csv
└── requirements.txt
```

---

## Installation

Clone the repository and install the required packages:

```bash
pip install -r requirements.txt
```

---

## Input File

Create an `identifiers.txt` file containing one resource identifier per line.

Example:

```text
RESOURCE-001
RESOURCE-002
RESOURCE-003
RESOURCE-004
```

---

## Running the Mock API

The repository includes a local mock API that simulates an external REST service.

Start the mock server:

```bash
python mock_api.py
```

The API will be available at:

```text
http://127.0.0.1:5000/v1/resources/metrics
```

The mock server returns demonstration JSON responses, allowing the project to be tested without relying on external services.

---

## Running the Monitor

Execute the monitoring script:

```bash
python main.py \
    --api-url http://127.0.0.1:5000/v1/resources/metrics
```

The script will:

1. Read resource identifiers from `identifiers.txt`
2. Send a request for each resource
3. Parse the JSON response
4. Update the historical CSV report
5. Save the results to `resource_metrics.csv`

---

## Example Output

After the first execution:

```csv
resource_id,2026-06-30 16:46:06
RESOURCE-001,431.69
RESOURCE-002,270.22
RESOURCE-003,339.74
```

Running the script again appends another timestamp column:

```csv
resource_id,2026-06-30 16:46:06,2026-06-30 16:52:30
RESOURCE-001,431.69,455.12
RESOURCE-002,270.22,281.44
RESOURCE-003,339.74,320.87
```

This allows metric history to be tracked over multiple executions.

---

## Custom Configuration

Specify custom files:

```bash
python main.py \
    --input identifiers.txt \
    --output report.csv
```

Change retry attempts:

```bash
python main.py \
    --retry-attempts 5
```

Change request timeout:

```bash
python main.py \
    --timeout 20
```

Customize delay between requests:

```bash
python main.py \
    --min-delay 2 \
    --max-delay 5
```

---

## Mock API

The included `mock_api.py` acts as a lightweight REST service.

It receives a resource identifier, generates a demonstration metric value, and returns a JSON response matching the structure expected by the monitoring script.

Workflow:

```
main.py
    │
    ▼
HTTP Request
    │
    ▼
mock_api.py
    │
    ▼
JSON Response
    │
    ▼
CSV Report
```

Using a local mock server allows the complete automation workflow to be tested without requiring API keys or access to production systems.

---

## Engineering Practices

This project demonstrates:

- REST API integration
- JSON processing
- Retry logic
- Timeout handling
- Historical reporting
- CSV data management
- CLI application design
- Configuration through arguments
- Local service mocking
- Reusable automation architecture

---

## Notes

This repository contains demonstration data only.

All resource identifiers, URLs, metric values, and API responses have been intentionally replaced with generic examples.

The project is designed to demonstrate automation architecture and implementation techniques rather than interact with any real production environment.

---

## Purpose

The goal of this project is to demonstrate how Python can be used to build reusable monitoring and reporting utilities that integrate with REST APIs while maintaining historical datasets suitable for automation, analytics, and operational reporting.
