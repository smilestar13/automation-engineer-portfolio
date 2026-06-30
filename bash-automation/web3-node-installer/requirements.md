# System Requirements

## Supported Operating Systems

The installer was originally developed and tested on:

- Ubuntu 22.04 LTS
- Ubuntu 24.04 LTS

Other Debian-based Linux distributions may also work but were not officially tested.

---

## Minimum Hardware Requirements

| Resource | Recommended |
|----------|-------------:|
| CPU | 2 vCPU |
| Memory | 4 GB RAM |
| Storage | 40 GB SSD |
| Network | Stable Internet connection |

---

## Required Permissions

The script requires:

- sudo privileges
- Internet access
- Ability to install system packages
- Permission to create Docker containers

---

## External Dependencies

The installer automatically downloads and configures the required software, including:

- Git
- Docker
- Docker Compose
- Node.js
- npm
- curl
- jq
- build-essential

No manual installation of these components is required before running the installer.

---

## Network Requirements

The server should have unrestricted outbound access to:

- GitHub
- Docker Hub
- Ubuntu package repositories
- Project-related package repositories

---

## Notes

This installer was designed for a clean Ubuntu server.

Running it on systems with heavily customized environments may require additional adjustments.
