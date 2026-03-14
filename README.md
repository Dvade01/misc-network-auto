This README is designed to help you (and others) understand how to set up and use your backup script. It follows standard NetDevOps documentation practices by including prerequisites, installation steps, and a clear description of what the script does.
Cisco IOS Config Backup Script
A Python-based automation tool that connects to multiple Cisco IOS devices via SSH to retrieve and save their running configurations to a local directory.

Overview


Automated Backups: Connects to a list of defined Cisco devices.
Dynamic Naming: Automatically detects the device hostname or uses the IP address if a hostname isn't found.
Organized Storage: Saves all configs into a backups/ folder with precise timestamps.
Error Handling: Continues to the next device if one connection fails, printing a clear error message.
Prerequisites:


Before running this script, ensure you have:
Python 3.x installed.
SSH enabled on your Cisco devices (CML virtual nodes or physical hardware).
Connectivity between your machine and the target management IPs.
Installation:


Clone or save the script to your local project folder.
Install dependencies using the pip package manager:
bash
pip install netmiko
Use code with caution.

Configuration:


Open the script and update the devices list with your specific network details:
python
devices = [
    {
        "device_type": "cisco_ios",
        "host": "YOUR_DEVICE_IP",
        "username": "YOUR_USERNAME",
        "password": "YOUR_PASSWORD",
        "secret": "YOUR_ENABLE_PASSWORD",
    }
]
Use code with caution.

Usage:


Run the script from your terminal or VS Code:
bash
python your_script_name.py
Use code with caution.

Upon successful execution, a folder named backups/ will be created in your directory containing files like Router01_2024-05-20_14-30-05.txt.
