import psutil
import os
import time
from datetime import datetime
from prometheus_client import start_http_server, Gauge

# Prometheus Metrics
cpu_gauge = Gauge('cpu_usage_percent', 'CPU Usage Percentage')
memory_gauge = Gauge('memory_usage_percent', 'Memory Usage Percentage')
disk_gauge = Gauge('disk_usage_percent', 'Disk Usage Percentage')

# Start Prometheus Metrics Server
start_http_server(8000)

print("Prometheus metrics available at http://localhost:8000/metrics")

while True:

    # Collect Metrics
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    # Network Check
    response = os.system("ping -c 1 google.com > /dev/null 2>&1")

    current_time = datetime.now()

    # Update Prometheus Metrics
    cpu_gauge.set(cpu)
    memory_gauge.set(memory)
    disk_gauge.set(disk)

    # CPU Status
    if cpu > 80:
        cpu_status = "CPU Critical"
    elif cpu > 50:
        cpu_status = "CPU Warning"
    else:
        cpu_status = "CPU Healthy"

    # Memory Status
    if memory > 80:
        memory_status = "Memory Critical"
    elif memory > 50:
        memory_status = "Memory Warning"
    else:
        memory_status = "Memory Healthy"

    # Disk Status
    if disk > 80:
        disk_status = "Disk Critical"
    elif disk > 50:
        disk_status = "Disk Warning"
    else:
        disk_status = "Disk Healthy"

    # Network Status
    if response == 0:
        network_status = "Network Healthy"
    else:
        network_status = "Network Down"

    # Console Output
    print("\n========== SERVER MONITOR ==========")
    print("Time:", current_time)
    print(f"CPU Usage: {cpu}% - {cpu_status}")
    print(f"Memory Usage: {memory}% - {memory_status}")
    print(f"Disk Usage: {disk}% - {disk_status}")
    print(f"Network Status: {network_status}")
    print("====================================")

    # Save Logs
    with open("monitor.log", "a") as file:
        file.write(
            f"{current_time} | "
            f"CPU={cpu}% ({cpu_status}) | "
            f"MEM={memory}% ({memory_status}) | "
            f"DISK={disk}% ({disk_status}) | "
            f"NETWORK={network_status}\n"
        )

    time.sleep(5)
