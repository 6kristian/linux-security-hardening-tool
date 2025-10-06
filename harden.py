#!/usr/bin/env python3
"""
Linux Security Hardening Tool by Kristian
"""

import subprocess
import os
from datetime import datetime

REPORT_FILE = "harden_report.txt"

def run_command(command):
    """Run a shell command and return output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error running command: {e}"

def check_updates():
    print("[+] Checking for system updates...")
    run_command("sudo apt update -qq")
    updates = run_command("apt list --upgradable 2>/dev/null | wc -l")
    return f"Packages with updates: {int(updates) - 1}"

def check_firewall():
    print("[+] Checking UFW (firewall) status...")
    ufw_status = run_command("sudo ufw status")
    if "active" in ufw_status.lower():
        return "Firewall is active ✅"
    return "Firewall is NOT active ⚠️"

def check_password_policy():
    print("[+] Checking password policy...")
    policy = run_command("grep -E 'PASS_MIN_LEN' /etc/login.defs")
    return policy if policy else "Could not find password policy."

def check_world_writable():
    print("[+] Searching for world-writable files...")
    files = run_command("find / -xdev -type f -perm -0002 2>/dev/null | head -n 5")
    return files if files else "No world-writable files found."

def check_root_ssh():
    print("[+] Checking if root SSH login is disabled...")
    sshd_config = run_command("grep -E '^PermitRootLogin' /etc/ssh/sshd_config")
    return sshd_config if sshd_config else "Could not verify SSH root login setting."

def save_report(results):
    with open(REPORT_FILE, "w") as f:
        f.write("===== LINUX SECURITY HARDENING REPORT =====\n")
        f.write(f"Generated on: {datetime.now()}\n\n")
        for section, output in results.items():
            f.write(f"[{section}]\n{output}\n\n")
    print(f"\n✅ Report saved to {REPORT_FILE}")

def main():
    print("===== LINUX SECURITY HARDENING TOOL =====\n")
    results = {
        "System Updates": check_updates(),
        "Firewall Status": check_firewall(),
        "Password Policy": check_password_policy(),
        "World Writable Files": check_world_writable(),
        "Root SSH Login": check_root_ssh(),
    }
    save_report(results)
    print("\n===== CHECK COMPLETE =====")

if __name__ == "__main__":
    main()



