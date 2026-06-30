# Ansible Node Backup

## Overview

This project demonstrates an Ansible playbook designed to automate the collection and backup of critical configuration files from multiple Linux servers.

The playbook connects to every host defined in the Ansible inventory, verifies the existence of important files, securely copies them to the control machine, and organizes the backups into host-specific directories.

This type of automation is commonly used to simplify backup procedures, disaster recovery, infrastructure migrations, and server maintenance.

---

## Business Scenario

Managing dozens or hundreds of Linux servers manually quickly becomes impractical.

When infrastructure administrators need to collect configuration files, identity keys, certificates, or service configuration from multiple machines, repetitive manual work increases the risk of mistakes.

This playbook automates the entire process by performing the collection in a consistent and repeatable way.

---

## Workflow

```text
Inventory Hosts
        │
        ▼
Connect via SSH
        │
        ▼
Check Required Files
        │
        ▼
Verify File Existence
        │
        ▼
Copy Existing Files
        │
        ▼
Store Files by Hostname
        │
        ▼
Report Missing Files
        │
        ▼
Backup Complete
```

---

## Features

- Multi-host automation
- Secure SSH execution
- Remote file verification
- Automatic backup collection
- Per-host backup directories
- Missing file reporting
- Controller-side storage
- Idempotent execution
- Inventory-based infrastructure management

---

## Technologies

- Ansible
- YAML
- SSH
- Linux
- Inventory Management

---

## Repository Structure

```text
ansible-node-backup/

├── README.md
└── node_backup.yml
```

---

## Example Directory Structure

After execution the controller will contain a backup similar to:

```text
node-backups/

├── server-01/
│   ├── identity.pem
│   ├── node-keypair.json
│   └── cluster-info.toml
│
├── server-02/
│   ├── identity.pem
│   ├── node-keypair.json
│   └── cluster-info.toml
│
└── server-03/
    ├── identity.pem
    ├── node-keypair.json
    └── cluster-info.toml
```

---

## Running the Playbook

```bash
ansible-playbook -i inventory node_backup.yml -f 15
```

---

## Engineering Practices

This project demonstrates:

- Infrastructure as Code (IaC)
- Configuration backup automation
- Multi-host orchestration
- Secure file collection
- Inventory-driven automation
- Remote file validation
- Controller delegation
- Modular Ansible playbooks
- Repeatable infrastructure operations

---

## Typical Use Cases

This workflow can be adapted for:

- Configuration backups
- Service migrations
- Disaster recovery preparation
- Cluster maintenance
- Infrastructure audits
- Secret and certificate collection
- Environment replication
- Scheduled backup automation

---

## Notes

This repository contains a **sanitized infrastructure automation example**.

All environment-specific paths, configuration names, infrastructure details, and business-specific implementation have been generalized for demonstration purposes while preserving the overall architecture and automation patterns.

The playbook illustrates common Ansible techniques that can be adapted to a wide variety of Linux infrastructure environments.

---

## Purpose

The goal of this project is to demonstrate practical experience with Ansible by automating a real-world infrastructure task that would otherwise require repetitive manual work across multiple servers.
