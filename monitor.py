import psutil
import os
from datetime import datetime

cpu = psutil.cpu_percent(interval=1)

memory = psutil.virtual_memory().percent

disk = psutil.disk_usage('/').percent

response = os.system("ping -n 1 google.com")

time = datetime.now()

if cpu > 80:
    print("CPU Critical:", cpu)

else:
    print("CPU Healthy:", cpu)


if memory > 80:
    print("Memory Critical:", memory)

else:
    print("Memory Healthy:", memory)


if disk > 80:
    print("Disk Critical:", disk)

else:
    print("Disk Healthy:", disk)

if response == 0:
    print("Network Healthy")

else:
    print("Network Down")

with open("monitor.log", "a") as file:

    file.write(f"\nTime: {time}\n")

    file.write(f"\nCPU Usage: {cpu}")

    file.write(f"\nMemory Usage: {memory}")

    file.write(f"\nDisk Usage: {disk}")

    if response == 0:
        file.write("\nNetwork Healthy\n")

    else:
        file.write("\nNetwork Down\n")

    