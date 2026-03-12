import psutil
import pandas as pd
from datetime import datetime
import os
print("hgeihit")

CSV_FILE = r"C:\Users\Kennedy N. Wilson\Desktop\PYTHON\system_monitor_log.csv"
EXCEL_FILE = r"C:\Users\Kennedy N. Wilson\Desktop\PYTHON\system_monitor.xlsx"

def collect_stats():
    return {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "CPU_Usage_%": psutil.cpu_percent(interval=1),
        "Memory_Usage_%": psutil.virtual_memory().percent,
        "Disk_Usage_%": psutil.disk_usage('C:\\').percent,
        "Network_Sent_MB": round(psutil.net_io_counters().bytes_sent / 1024 / 1024, 2),
        "Network_Recv_MB": round(psutil.net_io_counters().bytes_recv / 1024 / 1024, 2),
    }

def save_data(data):
    df = pd.DataFrame([data])

    if not os.path.exists(CSV_FILE):
        df.to_csv(CSV_FILE, index=False)
    else:
        df.to_csv(CSV_FILE, mode='a', header=False, index=False)

    df_all = pd.read_csv(CSV_FILE)
    df_all.to_excel(EXCEL_FILE, index=False)

if __name__ == "__main__":
    stats = collect_stats()
    save_data(stats)
    print("System data logged successfully!")
    print("System data logged successfully!")