# Array Min & Max Finder

## Overview

<img width="805" height="610" alt="image" src="https://github.com/user-attachments/assets/26092ac5-b697-4a4c-91ad-b5622766bad8" />

This UiPath workflow demonstrates how to process an array of numbers and identify the minimum and maximum values using a `For Each` loop.

The workflow starts with a predefined integer array, iterates through each value, compares it with the current minimum and maximum values, and displays the final result in a message box.

This project demonstrates core UiPath concepts such as arrays, loops, variables, conditional expressions, and multiple assignment operations.

---

## Business Scenario

Many automation workflows require processing lists of values and extracting useful information from them.

Typical examples include:

- finding minimum and maximum transaction values
- checking score ranges
- analyzing numeric datasets
- validating thresholds
- processing calculated values from Excel or APIs

This workflow demonstrates the basic logic behind such data processing tasks.

---

## Workflow

```text
Initialize Number Array
        │
        ▼
Set Initial Min / Max Values
        │
        ▼
Loop Through Each Number
        │
        ▼
Compare Current Number
        │
        ▼
Update Min / Max Values
        │
        ▼
Display Result
```

---

## Features

- Integer array processing
- `For Each` loop
- Minimum value detection
- Maximum value detection
- Multiple Assign activity
- Conditional expressions
- String formatting
- Result output with Message Box

---

## Technologies

- UiPath Studio
- UiPath System Activities
- VB.NET expressions
- XAML workflows

---

## Repository Structure

```text
for-each-and-if/

├── README.md
├── Main.xaml
└── project.json
```

---

## Example Input

```text
7, 5, 2, 4, 3, 9
```

---

## Example Output

```text
Test number array are: 7, 5, 2, 4, 3, 9
Min number from array is: 2
Max number from array is: 9
```

---

## Skills Demonstrated

- Variables
- Arrays
- For Each loop
- Multiple Assign
- Conditional logic
- Numeric comparison
- String.Join
- Message Box output

---

## Purpose

This project was created to demonstrate how UiPath can process arrays and apply basic comparison logic to calculate minimum and maximum values.
