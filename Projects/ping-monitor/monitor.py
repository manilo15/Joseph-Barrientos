import os
import time
from datetime import datetime

target = "8.8.8.8"
log_file = "logs/monitor_log.txt"


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


print(f"Monitoring {target}...\nPress Ctrl+C to stop.\n")

while True:
    response = os.system(f"ping -n 1 {target} > nul")

    if response == 0:
        print(f"{target} is UP")
        log(f"{target} is UP")
    else:
        print(f"{target} is DOWN")
        log(f"{target} is DOWN")

    time.sleep(2)
