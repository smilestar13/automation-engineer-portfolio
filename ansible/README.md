# Ansible Automation

## Overview

This directory contains a collection of Ansible playbooks demonstrating real-world infrastructure automation tasks commonly performed by Automation Engineers and DevOps Engineers.

The examples focus on automating repetitive server administration tasks across multiple Linux hosts using Infrastructure as Code (IaC) principles.

Rather than managing individual servers manually, these playbooks show how Ansible can orchestrate deployments, collect operational data, automate interactive installers, and simplify infrastructure management at scale.

---

## Included Projects

### Node Backup

Automates the collection of important configuration files from multiple Linux servers and stores them on the control machine using a structured per-host directory layout.

**Demonstrated concepts**

- Multi-host automation
- SSH execution
- Remote file verification
- Secure file collection
- Centralized backups
- Infrastructure migration support

---

### VPS Metrics Report

Collects operational metrics from multiple servers, parses command output, and automatically generates centralized CSV reports for infrastructure monitoring and operational visibility.

**Demonstrated concepts**

- Command execution
- Output parsing
- Data normalization
- CSV reporting
- Multi-host monitoring
- Infrastructure reporting

---

### Interactive Installer Automation

Automates interactive command-line installers using the Ansible **Expect** module.

The playbook downloads an installation script, automatically answers installer prompts, validates successful deployment, extracts generated identifiers, and stores deployment metadata.

**Demonstrated concepts**

- Interactive CLI automation
- Expect module
- Automated deployments
- Log validation
- Deployment tracking
- Infrastructure provisioning

---

## Engineering Practices

These projects demonstrate practical experience with:

- Infrastructure as Code (IaC)
- Multi-host automation
- Inventory management
- SSH orchestration
- Playbook development
- Remote command execution
- Configuration management
- Infrastructure monitoring
- Backup automation
- Automated deployments
- Log processing
- Data collection
- Idempotent automation
- Repeatable infrastructure operations

---

## Technologies

- Ansible
- YAML
- Linux
- SSH
- Jinja2
- Bash
- CSV Reporting

---

## Repository Structure

```text
ansible/

├── README.md
│
├── node_backup/
│   ├── README.md
│   └──node_backup.yml
│  
│
├── ansible-vps-metrics-report/
│   ├── README.md
│   └── node_metrics_collector.yml
│   
│
└── ansible-interactive-installer-automation/
    ├── README.md
    └─ interactive_installer.yml
 
```

---

## Purpose

The goal of this collection is to demonstrate practical Ansible skills through real infrastructure automation scenarios.

Each project focuses on solving operational tasks that commonly arise when managing Linux servers, cloud infrastructure, and distributed environments.

The examples illustrate how repetitive administrative processes can be transformed into reliable, reusable, and scalable automation workflows.

---

## Disclaimer

Several repositories contain **sanitized versions** of production automation projects.

Infrastructure-specific information such as:

- server addresses
- service names
- deployment identifiers
- credentials
- inventory data
- repository URLs
- business logic

has been intentionally replaced with generic placeholders while preserving the architecture, engineering practices, and automation techniques demonstrated by the original implementations.

---

## Skills Demonstrated

- Infrastructure as Code
- Configuration Management
- Linux Administration
- SSH Automation
- Multi-Host Orchestration
- Interactive CLI Automation
- Infrastructure Monitoring
- Backup Automation
- Log Validation
- Deployment Automation
- YAML Development
- Automation Engineering
- DevOps Fundamentals
