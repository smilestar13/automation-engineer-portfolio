# Ansible Node Metrics Collector

## Overview

This project demonstrates an Ansible playbook designed to collect operational metrics from multiple Linux servers and generate a consolidated CSV report on the control machine.

The playbook executes the same command across every host in the inventory, extracts key performance metrics from the command output, normalizes the collected data, and automatically builds a centralized report.

This type of automation is commonly used for infrastructure monitoring, operational reporting, capacity planning, and scheduled health checks.

---

## Business Scenario

Infrastructure teams often need to monitor dozens or hundreds of servers running the same service.

Collecting operational metrics manually from each machine is time-consuming and error-prone.

This playbook automates the process by:

- Connecting to every server via SSH
- Executing a monitoring command
- Parsing the returned output
- Extracting important metrics
- Generating a consolidated CSV report

The resulting report can be used for operational dashboards, scheduled reports, or infrastructure audits.

---

## Workflow

```text
Inventory Hosts
        │
        ▼
Connect via SSH
        │
        ▼
Execute Monitoring Command
        │
        ▼
Capture Output
        │
        ▼
Parse Metrics
        │
        ▼
Normalize Values
        │
        ▼
Generate CSV Report
        │
        ▼
Infrastructure Summary
```

---

## Features

- Multi-host metric collection
- SSH-based execution
- Command output parsing
- Automatic data normalization
- CSV report generation
- Controller-side aggregation
- Inventory-based automation
- Idempotent execution
- Fault-tolerant collection
- Daily report generation

---

## Technologies

- Ansible
- YAML
- Linux
- SSH
- CSV Reporting
- Jinja2 Templates
- Regular Expressions

---

## Repository Structure

```text
ansible-node-metrics-collector/

├── README.md
└── node_metrics_collector.yml

```

---

## Generated Report

After execution a report similar to the following is generated:

```csv
hostname,metric_value,multiplier,tier,uptime,allocation

server-01,1250,1.20,3,98.2,45
server-02,1188,1.10,2,99.8,42
server-03,1327,1.35,4,97.4,48
```

The report provides a centralized overview of service status across all managed servers.

---

## Running the Playbook

```bash
ansible-playbook -i inventory node_metrics_collector.yml -f 15
```

---

## Engineering Practices

This project demonstrates:

- Infrastructure as Code (IaC)
- Multi-host automation
- Centralized reporting
- Command execution
- Output parsing
- Regular expression processing
- Data normalization
- CSV generation
- Inventory-driven infrastructure management
- Controller delegation

---

## Typical Use Cases

This workflow can be adapted for:

- Infrastructure monitoring
- Service health reporting
- Resource utilization tracking
- Capacity planning
- Cluster monitoring
- Scheduled operational reports
- Fleet management
- Periodic infrastructure audits

---

## Notes

This repository contains a **sanitized infrastructure automation example**.

All environment-specific paths, service names, commands, metrics, and implementation details have been generalized for demonstration purposes while preserving the overall automation architecture.

The playbook demonstrates common Ansible techniques for collecting operational information from multiple Linux servers.

---

## Purpose

The goal of this project is to demonstrate practical experience with Ansible by automating infrastructure-wide metric collection and generating centralized operational reports from multiple managed hosts.
