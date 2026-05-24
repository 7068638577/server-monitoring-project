import psutil
import os
import time
from datetime import datetime

while True:

    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    response = os.system("ping -c 1 google.com > /dev/null 2>&1")

    current_time = datetime.now()

    # CPU Condition
    if cpu > 80:
        cpu_status = "CPU Critical"
    elif cpu > 50:
        cpu_status = "CPU Warning"
    else:
        cpu_status = "CPU Healthy"

    # Memory Condition
    if memory > 80:
        memory_status = "Memory Critical"
    elif memory > 50:
        memory_status = "Memory Warning"
    else:
        memory_status = "Memory Healthy"

    # Disk Condition
    if disk > 80:
        disk_status = "Disk Critical"
    elif disk > 50:
        disk_status = "Disk Warning"
    else:
        disk_status = "Disk Healthy"

    # Network Condition
    if response == 0:
        network_status = "Network Healthy"
    else:
        network_status = "Network Down"

    # Print Output
    print("\n========== SERVER MONITOR ==========")

    print("Time:", current_time)

    print(f"CPU Usage: {cpu}% - {cpu_status}")

    print(f"Memory Usage: {memory}% - {memory_status}")

    print(f"Disk Usage: {disk}% - {disk_status}")

    print(network_status)

    print("====================================")

    # Save Logs
    with open("monitor.log", "a") as file:

        file.write(f"\nimport psutil
import os
import time
from datetime import datetime

while True:

    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    response = os.system("ping -c 1 google.com > /dev/null 2>&1")

    current_time = datetime.now()

    # CPU Condition
    if cpu > 80:
        cpu_status = "CPU Critical"
    elif cpu > 50:
        cpu_status = "CPU Warning"
    else:
        cpu_status = "CPU Healthy"

    # Memory Condition
    if memory > 80:
        memory_status = "Memory Critical"
    elif memory > 50:
        memory_status = "Memory Warning"
    else:
        memory_status = "Memory Healthy"

    # Disk Condition
    if disk > 80:
        disk_status = "Disk Critical"
    elif disk > 50:
        disk_status = "Disk Warning"
    else:
        disk_status = "Disk Healthy"

    # Network Condition
    if response == 0:
        network_status = "Network Healthy"
    else:
        network_status = "Network Down"

    # Print Output
    print("\n========== SERVER MONITOR ==========")

    print("Time:", current_time)

    print(f"CPU Usage: {cpu}% - {cpu_status}")

    print(f"Memory Usage: {memory}% - {memory_status}")

    print(f"Disk Usage: {disk}% - {disk_status}")

    print(network_status)

    print("====================================")

    # Save Logs
    with open("monitor.log", "a") as file:

        file.write(f"\n
