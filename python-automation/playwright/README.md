# Playwright Browser Extension Workflow

## Overview

This project demonstrates a production-inspired browser automation workflow built with **Playwright**.

The workflow illustrates how browser extensions, persistent browser profiles, multi-page interactions, JavaScript execution, and dashboard monitoring can be orchestrated into a single automation process.

This repository focuses on automation architecture rather than a specific business domain.

---

## Business Scenario

Many enterprise web applications require users to:

- authenticate through browser extensions
- work inside isolated browser profiles
- interact with dynamic web interfaces
- approve multiple browser dialogs
- monitor dashboard values
- periodically collect operational metrics

This workflow demonstrates how these repetitive browser operations can be automated using Playwright.

---

## Workflow Overview

```
Browser Profile
        │
        ▼
Load Browser Extension
        │
        ▼
Initialize Extension Session
        │
        ▼
Authenticate Portal
        │
        ▼
Handle Extension Popups
        │
        ▼
Execute JavaScript
        │
        ▼
Read Dashboard Metrics
        │
        ▼
Save Metric History
```

---

## Features

- Playwright browser automation
- Persistent browser profiles
- Browser extension integration
- Multi-page workflow handling
- Popup management
- JavaScript execution
- Dynamic UI interaction
- Dashboard monitoring
- Metric logging
- Continuous background monitoring
- Modular workflow design

---

## Technologies

- Python 3
- Playwright
- Chromium
- JavaScript
- Browser Extensions

---

## Repository Structure

```text
playwright/

├── README.md
├── main.py
├── requirements.txt
├── auth_data.example.txt
└── metrics_history.txt
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browser binaries:

```bash
playwright install chromium
```

---

## Configuration

The workflow expects an authentication data file in the following format:

```text
ExampleWord01 ExampleWord02 ExampleWord03 ExampleWord04 ExampleWord05 ExampleWord06 ExampleWord07 ExampleWord08 ExampleWord09 ExampleWord10 ExampleWord11 ExampleWord12
```

A sample file is included:

```text
auth_data.example.txt
```

---

## Monitoring

During execution the workflow periodically reads a dashboard metric and appends timestamped entries to:

```text
metrics_history.txt
```

Example:

```text
2026-06-30 14:00:00 - Metric value: 152
2026-06-30 14:05:00 - Metric value: 161
2026-06-30 14:10:00 - Metric value: 174
```

This demonstrates how automation workflows can continuously collect operational data for reporting purposes.

---

## Workflow Components

The project demonstrates several common browser automation techniques:

- Browser profile management
- Extension initialization
- Authentication workflow
- Popup handling
- Dynamic page interaction
- JavaScript execution
- Dashboard monitoring
- Periodic metric collection

---

## Engineering Practices

This project demonstrates:

- Modular function design
- Browser automation architecture
- Reusable workflow organization
- Error handling
- Continuous monitoring patterns
- Browser extension automation
- Production-style Playwright implementation

---

## Notes

This repository contains a **sanitized version of a real automation workflow**.

To protect confidential information, all business-specific implementation details have been replaced with generic placeholders, including:

- URLs
- Browser extensions
- Selectors
- Credentials
- Authentication data
- Portal names
- Dashboard values
- Business logic

The overall workflow architecture and automation patterns have been preserved while removing all sensitive implementation details.

This project is intended to demonstrate browser automation design and engineering practices rather than interact with any real production environment.

---

## Purpose

The goal of this project is to demonstrate how Playwright can be used to automate enterprise browser workflows involving browser extensions, authentication, JavaScript execution, and continuous dashboard monitoring.
