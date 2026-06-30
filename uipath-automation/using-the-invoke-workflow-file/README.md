# Deposit Interest Calculator

## Overview
<img width="571" height="976" alt="image" src="https://github.com/user-attachments/assets/f05a80d7-cadb-4247-8d47-069636ee809f" />
<img width="263" height="503" alt="image" src="https://github.com/user-attachments/assets/e40b0071-abba-4ce2-99fb-3986288e80b6" />
<img width="285" height="253" alt="image" src="https://github.com/user-attachments/assets/bfdee723-853b-41e6-abb2-9cb98c6ca012" />
<img width="329" height="212" alt="image" src="https://github.com/user-attachments/assets/1568ff78-17a9-4b39-b8c0-9816425d1222" />

This UiPath workflow automates a simple deposit interest calculation process.

The robot asks the user to enter an initial deposit amount, validates the input, allows up to three attempts, lets the user choose a deposit period, and then calculates the expected earnings using a separate reusable workflow file.

This project demonstrates core UiPath concepts such as variables, validation, loops, arguments, business rules, and workflow modularity.

---

## Workflow

```text
Input Deposit Amount
        │
        ▼
Validate Numeric Input
        │
        ▼
Retry Up To 3 Attempts
        │
        ▼
Choose Deposit Period
        │
        ▼
Invoke Calculation Workflow
        │
        ▼
Display Final Result
