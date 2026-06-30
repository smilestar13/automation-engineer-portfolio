# Vegetables Production Report

## Overview

<img width="806" height="652" alt="image" src="https://github.com/user-attachments/assets/f5cf9fac-90b7-4710-979b-6b2be565eb6b" />
<img width="810" height="549" alt="image" src="https://github.com/user-attachments/assets/3ff0304b-01ad-4778-999e-690173581501" />
<img width="762" height="551" alt="image" src="https://github.com/user-attachments/assets/7435f347-ced1-4624-87b5-a1b915e1f3ac" />
<img width="743" height="550" alt="image" src="https://github.com/user-attachments/assets/6f726bb8-dcae-4b12-aad5-60e61f57bd10" />

This UiPath workflow automates Excel-based production reporting.

The robot reads production data from an Excel workbook, adds a new calculated column, calculates estimated values for each row, writes the processed data back to Excel, formats currency values, creates a Pivot Table, and generates a chart for visual reporting.

This project demonstrates practical Excel automation using both classic workbook activities and modern Excel activities.

---

## Business Scenario

A production department tracks vegetable quantities and prices in an Excel file.

Instead of manually calculating estimated values, creating summaries, and building charts, this workflow automates the reporting process.

Typical use cases include:

- production tracking
- inventory valuation
- sales estimation
- Excel report generation
- monthly operational reporting
- automated business dashboards

---

## Workflow

```text
Read Excel Data
        │
        ▼
Add Estimated Value Column
        │
        ▼
Calculate Row Values
        │
        ▼
Write Updated Data
        │
        ▼
Format Currency Column
        │
        ▼
Create Pivot Table
        │
        ▼
Insert Chart
```

---

## Features

- Excel data reading
- DataTable processing
- Dynamic column creation
- Row-by-row calculations
- Currency formatting
- Pivot Table creation
- Excel chart generation
- Automated report preparation

---

## Technologies

- UiPath Studio
- UiPath Excel Activities
- UiPath Modern Excel Activities
- DataTable
- VB.NET expressions
- XAML workflows

---

## Repository Structure

```text
vegetables-production-report/

├── README.md
├── Main.xaml
├── project.json
└── VegetablesProduction.xlsx
```

---

## Input Data

The workflow expects an Excel workbook:

```text
VegetablesProduction.xlsx
```

with a sheet named:

```text
Tracker
```

The input data should include columns such as:

```text
Vegetables
Quantity
Price per Kg
```

---

## Output

The workflow creates or updates:

```text
EstimatedValues
VegetablesPivot
```

The final workbook includes:

- calculated estimated values
- formatted currency column
- Pivot Table summary
- column chart visualization

---

## Example Calculation

```text
Estimated Value = Quantity × Price per Kg
```

Example:

```text
Quantity: 120
Price per Kg: 2.50
Estimated Value: 300.00 €
```

---

## Skills Demonstrated

- Excel automation
- DataTable usage
- Add Data Column
- For Each Row
- Write Range
- Excel Process Scope
- Use Excel File
- Format Cells
- Pivot Table
- Insert Chart
- Report generation

---

## Purpose

This project demonstrates how UiPath can automate Excel reporting workflows by combining data processing, calculations, formatting, Pivot Tables, and charts into a complete business report.
