# 🛡️ Linux Security Hardening Tool

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/6kristian/linux-security-hardening-tool)](https://github.com/6kristian/linux-security-hardening-tool/issues)
[![GitHub stars](https://img.shields.io/github/stars/6kristian/linux-security-hardening-tool)](https://github.com/6kristian/linux-security-hardening-tool/stargazers)

A Python-based tool to audit and harden Linux system security configurations.  
Automates common security checks, generates reports, and reduces manual auditing effort.

---

## Features

- ✅ Checks for available system updates  
- ✅ Verifies UFW (firewall) status  
- ✅ Checks password policy compliance  
- ✅ Finds world-writable files  
- ✅ Detects SSH root login permissions  
- ✅ Generates a detailed report (`harden_report.txt`)  

---

## Usage

1. Clone the repository:
```bash
git clone git@github.com:6kristian/linux-security-hardening-tool.git
cd linux-security-hardening-tool
```
## **Getting Started with Docker**

### **1. Pull the Docker image**

```bash
docker pull kristian6/linux-harden-tool:latest
```

### **2. Run the tool**

```bash
docker run -it --rm kristian6/linux-harden-tool:latest
```

> If the script requires root-level actions, use:

```bash
docker run -it --rm --privileged kristian6/linux-harden-tool:latest
```

