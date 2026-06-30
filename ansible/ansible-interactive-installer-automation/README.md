# Ansible Interactive Installer Automation

## Overview

This project demonstrates an Ansible playbook that automates an interactive command-line installation process using the **expect** module.

Many enterprise installers still rely on interactive terminal prompts, making them difficult to automate using traditional configuration management tools. This playbook demonstrates how Ansible can fully automate those workflows while validating the installation and recording deployment information.

The workflow is designed to transform a manual, error-prone installation process into a repeatable Infrastructure as Code deployment.

---

## Business Scenario

Infrastructure teams often need to deploy the same service across multiple Linux servers.

When the installer requires manual input such as:

- account identifiers
- authentication keys
- service addresses
- RPC endpoints
- confirmation prompts

deployment becomes slow, inconsistent and difficult to scale.

This playbook automates the complete installation process without manual interaction.

---

## Workflow

```text
Inventory Hosts
        │
        ▼
Connect via SSH
        │
        ▼
Download Installer
        │
        ▼
Check Existing Deployment
        │
        ▼
Launch Interactive Installer
        │
        ▼
Automatically Answer Prompts
        │
        ▼
Validate Installation
        │
        ▼
Extract Generated Identifiers
        │
        ▼
Save Deployment Metadata
        │
        ▼
Deployment Complete
```

---

## Features

- Interactive CLI automation
- Ansible Expect module
- Automated installer execution
- Remote script deployment
- SSH automation
- Log validation
- Metadata extraction
- Deployment tracking
- Controller-side record keeping
- Repeatable infrastructure deployment

---

## Technologies

- Ansible
- YAML
- Linux
- SSH
- Bash
- Expect Module

---

## Repository Structure

```text
ansible-interactive-installer-automation/

├── README.md
└── interactive_installer.yml
```

---

## Running the Playbook

```bash
ansible-playbook -i inventory interactive_installer.yml -f 15
```

---

## Deployment Workflow

The playbook automatically performs the following operations:

1. Downloads the installation script.
2. Searches for previously generated deployment information.
3. Executes the interactive installer.
4. Responds to installer prompts automatically.
5. Verifies successful installation.
6. Extracts generated deployment identifiers.
7. Stores deployment metadata on the control machine.

---

## Engineering Practices

This project demonstrates:

- Infrastructure as Code (IaC)
- Interactive CLI automation
- Ansible Expect automation
- Remote deployment
- Installation validation
- Log parsing
- Deployment metadata management
- Multi-host infrastructure automation
- Repeatable provisioning workflows

---

## Typical Use Cases

This automation pattern can be adapted for:

- Interactive software installers
- Internal deployment utilities
- Infrastructure provisioning
- Service registration
- Cluster deployment
- Secure onboarding workflows
- Automated server initialization
- Enterprise software installation

---

## Notes

This repository contains a **sanitized infrastructure automation example**.

To protect confidential implementation details, all environment-specific information has been replaced with generic placeholders, including:

- installation sources
- server addresses
- authentication data
- deployment identifiers
- service names
- infrastructure configuration

The deployment workflow and automation techniques have been preserved to demonstrate practical Ansible engineering patterns.

---

## Purpose

The goal of this project is to demonstrate how Ansible can automate interactive command-line installers using the **Expect** module, validate deployment success, and record installation metadata in a repeatable and scalable way.

Unlike simple configuration playbooks, this example illustrates automation of software that normally requires manual user interaction, making it particularly valuable for large-scale infrastructure deployments.
