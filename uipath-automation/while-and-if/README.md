# Guess The Number Game

## Overview

<img width="810" height="685" alt="image" src="https://github.com/user-attachments/assets/6e5836af-2f07-4236-913f-b7965bd61a10" />
<img width="815" height="560" alt="image" src="https://github.com/user-attachments/assets/6d3491c7-0c4f-4c94-9650-ca4d32939935" />
<img width="813" height="554" alt="image" src="https://github.com/user-attachments/assets/eb1ee36e-7880-47f0-b43f-ac452db4729d" />

This UiPath workflow implements a classic "Guess the Number" game to demonstrate core programming concepts within UiPath.

The robot generates a random secret number, asks the user to guess it, validates the entered value, provides hints after each attempt, and finishes when the correct number is found or all attempts are used.

Although simple, this project demonstrates many fundamental UiPath concepts that are commonly used in business automation workflows.

---

## Business Scenario

Interactive workflows often require users to repeatedly enter information until valid data is received or a predefined condition is met.

Typical real-world examples include:

- validation of customer input
- approval workflows
- confirmation dialogs
- interactive attended automations
- user-guided business processes

This project demonstrates how such logic can be implemented using UiPath.

---

## Workflow

```text
Generate Random Number
        │
        ▼
Show Welcome Message
        │
        ▼
Ask User For Number
        │
        ▼
Validate Input
        │
        ▼
Compare With Secret Number
        │
        ├───────────────┐
        ▼               ▼
Too High          Too Low
        │               │
        └──────┬────────┘
               ▼
Decrease Attempts
               │
               ▼
Correct?
        │
   Yes ─┴─ No
        │
        ▼
Display Result
```

---

## Features

- Random number generation
- Interactive user input
- Numeric validation
- Retry logic
- Limited number of attempts
- Conditional branching
- While loop
- User feedback
- Success and failure handling

---

## Technologies

- UiPath Studio
- UiPath System Activities
- VB.NET expressions
- XAML workflows

---

## Repository Structure

```text
while-and-if/

├── README.md
├── Main.xaml
└── project.json
```

---

## Example Gameplay

```text
Welcome to Guess The Number!

Guess a number between 1 and 50.

Attempt #1
> 20

Your number is a little bit lower.
2 attempts left.

Attempt #2
> 35

Your number is a little bit higher.
1 attempt left.

Attempt #3
> 28

Congratulations!
28 is the correct answer.
```

---

## Skills Demonstrated

- Variables
- While Loop
- Integer Validation
- Integer.TryParse
- Random Number Generation
- If / Else If Logic
- Boolean Variables
- User Interaction
- Message Boxes
- Input Dialog
- Conditional Expressions

---

## Purpose

This project was created to demonstrate interactive workflow design in UiPath using loops, user input validation, conditional logic, and basic game mechanics.

While implemented as a simple game, the same workflow patterns can be applied to real business processes that require repeated user interaction, validation, and decision making.
