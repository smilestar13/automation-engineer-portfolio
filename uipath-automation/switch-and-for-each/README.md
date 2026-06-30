# Error Code Classifier

## Overview

<img width="809" height="686" alt="image" src="https://github.com/user-attachments/assets/6f1cfc75-0bbb-46a6-adfd-50522924704b" />
<img width="809" height="551" alt="image" src="https://github.com/user-attachments/assets/158b3061-8076-42bd-aa9d-338fc2525601" />
<img width="811" height="546" alt="image" src="https://github.com/user-attachments/assets/89956341-1db9-41c2-a008-a14b40ca3f89" />

This UiPath workflow demonstrates how to classify a list of codes into separate categories using a `For Each` loop and a `Switch` activity.

The robot iterates through an input array, checks the prefix of each code, routes it into the correct category array, and collects invalid or unexpected codes into a separate list.

This project demonstrates practical data classification logic that can be reused in business automation scenarios.

---

## Business Scenario

Many business processes require records to be grouped by type, prefix, status, department, region, or error category.

Typical use cases include:

- classifying error codes
- grouping transaction IDs
- sorting customer records by prefix
- separating document types
- routing cases to different processing queues
- detecting invalid or unexpected records

This workflow demonstrates the basic pattern behind such routing and classification logic.

---

## Workflow

```text
Input Code Array
        │
        ▼
Loop Through Each Code
        │
        ▼
Read Code Prefix
        │
        ▼
Switch By Prefix
        │
        ├── Ax → AxArray
        ├── Bx → BxArray
        ├── Cx → CxArray
        └── Other → BrokenArray
        │
        ▼
Display Classification Result
```

---

## Features

- String array processing
- `For Each` loop
- `Switch` activity
- Prefix-based routing
- Dynamic array updates
- Invalid code detection
- Warning log messages
- Formatted result output

---

## Technologies

- UiPath Studio
- UiPath System Activities
- VB.NET expressions
- XAML workflows

---

## Repository Structure

```text
error-code-classifier/

├── README.md
├── Main.xaml
└── project.json
```

---

## Example Input

```text
Ax001, Ax002, Ax003, Ax004, Ax005,
Bx001, Bx002, Bx003,
Cx001, Cx002, Cx003, Cx004
```

---

## Example Output

```text
Ax Codes: Ax001, Ax002, Ax003, Ax004, Ax005
Bx Codes: Bx001, Bx002, Bx003
Cx Codes: Cx001, Cx002, Cx003, Cx004

✓ No invalid error codes were detected.
```

---

## Skills Demonstrated

- Variables
- Arrays
- For Each
- Switch activity
- String manipulation
- Substring
- Array concatenation
- Log Message
- Conditional output
- Message Box

---

## Purpose

This project was created to demonstrate how UiPath can classify structured values using prefixes and route them into separate collections.

Although the example uses simple demo codes, the same pattern can be applied to real-world workflows involving document routing, transaction classification, error handling, and business rule processing.
