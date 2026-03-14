from netmiko import ConnectHandler
from datetime import datetime
from pathlib import Path

# List of devices to back up
devices = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.10",
        "username": "admin",
        "password": "password123",
        "secret": "enablepassword",
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.11",
        "username": "admin",
        "password": "password123",
        "secret": "enablepassword",
    },
]

# Create backup folder if it does not exist
backup_dir = Path("backups")
backup_dir.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

for device in devices:
    try:
        print(f"Connecting to {device['host']}...")

        connection = ConnectHandler(**device)
        connection.enable()

        hostname_output = connection.send_command("show running-config | include hostname")
        if "hostname" in hostname_output:
            hostname = hostname_output.split()[-1]
        else:
            hostname = device["host"]

        running_config = connection.send_command("show running-config")

        filename = backup_dir / f"{hostname}_{timestamp}.txt"
        with open(filename, "w") as file:
            file.write(running_config)

        print(f"Backup saved: {filename}")
        connection.disconnect()

    except Exception as e:
        print(f"Failed to back up {device['host']}: {e}")
