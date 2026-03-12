import psutil
import csv
from datetime import datetime
import os

OUTPUT_FILE = "system_monitor_log.csv"

# Create file + header if not exists
if not os.path.exists(OUTPUT_FILE):
    with open(OUTPUT_FILE, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Timestamp",
            "CPU_Usage_Percent",
            "Memory_Usage_Percent",
            "Disk_Usage_Percent",
            "Network_Sent_MB",
            "Network_Received_MB"
        ])

# Capture metrics ONCE
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('C:\\').percent

net = psutil.net_io_counters()
sent_mb = net.bytes_sent / (1024 * 1024)
recv_mb = net.bytes_recv / (1024 * 1024)

# Write single row
with open(OUTPUT_FILE, mode="a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        timestamp,
        cpu,
        memory,
        disk,
        round(sent_mb, 2),
        round(recv_mb, 2)
    ])

print("System health captured once and saved successfully.")