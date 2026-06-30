# Flight Reservation Form

## Overview

<img width="305" height="461" alt="image" src="https://github.com/user-attachments/assets/7be1049b-2e2e-4e7d-b96f-d8b0c5d60f18" />
<img width="808" height="410" alt="image" src="https://github.com/user-attachments/assets/3680aec4-2bf2-4811-89b1-f66ee19050fc" />

This UiPath workflow demonstrates a form-based flight reservation process.

The robot opens a custom UiPath Form, collects reservation details from the user, stores the submitted values in variables, formats the data into a structured reservation summary, and writes the final confirmation to a text file.

This project demonstrates how UiPath Forms can be used to build user-friendly input interfaces for attended automation workflows.

---

## Business Scenario

Many business processes require structured user input before automation can continue.

Instead of using multiple separate input dialogs, this workflow uses a single form to collect all required reservation information in one place.

Typical use cases include:

- travel request forms
- internal reservation workflows
- employee request forms
- approval preparation
- structured data collection
- attended automation input screens

---

## Workflow

```text
Open Reservation Form
        │
        ▼
Collect User Input
        │
        ▼
Store Form Values
        │
        ▼
Format Reservation Data
        │
        ▼
Generate Confirmation Text
        │
        ▼
Save Confirmation File
```

---

## Features

- UiPath Forms integration
- Structured user input
- Date and time fields
- Form output arguments
- Variable mapping
- String array creation
- Date formatting
- Text file generation
- Attended automation workflow

---

## Technologies

- UiPath Studio
- UiPath Forms
- UiPath System Activities
- VB.NET expressions
- XAML workflows

---

## Repository Structure

```text
flight-reservation-form/

├── README.md
├── Main.xaml
├── project.json
└── ReservationConfirmation.txt
```

---

## Output Example

The workflow generates a confirmation file similar to:

```text
Flight Reservation Confirmation

Destination: Vienna
Departure Date: 15.07.2026 10:30
Return Date: 20.07.2026 18:45
Baggage: Additional cabin baggage
```

---

## Skills Demonstrated

- UiPath Forms
- Variables
- DateTime handling
- In/Out form arguments
- Assign activities
- String arrays
- Text file writing
- Data formatting
- Attended automation design

---

## Purpose

This project demonstrates how UiPath can be used to collect structured user input through forms and generate formatted output files for business workflows.
