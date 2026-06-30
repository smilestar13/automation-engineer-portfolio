# Selenium Email OTP Login

## Overview

This project demonstrates one component of an enterprise email automation workflow.

The script automates the process of authenticating to a protected web portal using a one-time verification code (OTP) received via email.

In production environments, this type of automation is commonly executed on Linux servers and is typically triggered by scheduled jobs (Cron), Bash scripts, health check routines, or orchestration systems whenever a new authentication session is required.

This repository focuses on the email verification workflow only, which represents one reusable module of a larger automation platform.

---

## Business Scenario

Many internal enterprise systems use email-based verification during authentication.

Instead of requiring an operator to:

- open the browser
- enter an email address
- wait for the verification email
- copy the verification code
- return to the browser
- complete authentication

this workflow performs the entire process automatically.

Such automation is particularly useful for unattended server-side processes and long-running automation services.

---

## Workflow Overview

```
Automation Trigger
(Cron / Bash / Health Check)
            │
            ▼
Launch Browser
            │
            ▼
Open Login Portal
            │
            ▼
Enter Email Address
            │
            ▼
Request Verification Code
            │
            ▼
Connect to IMAP Mailbox
            │
            ▼
Locate Latest Verification Email
            │
            ▼
Extract OTP Code
            │
            ▼
Complete Authentication
            │
            ▼
Continue Automation Workflow
```

---

## Features

- Selenium browser automation
- Headless Chrome execution
- IMAP email integration
- Automatic OTP retrieval
- Verification code parsing
- Email timestamp validation
- Retry mechanism
- Timeout handling
- Environment configuration
- Server-friendly execution
- Reusable authentication module

---

## Technologies

- Python 3
- Selenium
- IMAPClient
- Pyzmail
- ChromeDriver Manager
- Gmail IMAP
- Threading

---

## Repository Structure

```text
selenium-email-otp-login/

├── README.md
├── main.py
└── requirements.txt
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a local configuration file based on:

```text
.env.email.example
```

Example:

```text
EMAIL=example@email.com
EMAIL_PASSWORD=ExampleAppPassword
IMAP_SERVER=imap.gmail.com
IMAP_PORT=993
IMAP_FOLDER=INBOX
```

For Gmail, an **App Password** should be used instead of the account password.

---

## Execution

Run the workflow:

```bash
python main.py
```

The automation will:

1. Open the login portal.
2. Enter the configured email address.
3. Request a verification code.
4. Connect to the IMAP mailbox.
5. Search for the newest verification email.
6. Extract the OTP code.
7. Complete browser authentication.

---

## Typical Server Usage

This script is designed as a reusable authentication component.

In production environments it is commonly executed by:

- Cron jobs
- Bash automation scripts
- Health check routines
- Infrastructure automation
- Long-running monitoring services
- RPA workflows
- CI/CD maintenance tasks

Rather than acting as a standalone application, it is intended to be one building block inside a larger automation ecosystem.

---

## Engineering Practices

This project demonstrates:

- Browser automation
- Secure email integration
- OTP verification workflows
- IMAP communication
- Environment-based configuration
- Error handling
- Timeout management
- Retry logic
- Headless execution
- Modular automation design

---

## Notes

This repository contains a **sanitized demonstration** of a production automation workflow.

All business-specific implementation details have been intentionally replaced with generic placeholders, including:

- Portal URLs
- CSS selectors
- Authentication flows
- Email addresses
- Credentials
- Verification messages
- Business logic

The overall workflow architecture has been preserved while removing confidential implementation details.

This project demonstrates automation techniques only and is not intended to interact with any real production environment.

---

## Purpose

The purpose of this repository is to demonstrate how Selenium and IMAP can be combined to automate email-based authentication workflows that are commonly used as reusable components within enterprise automation platforms.
