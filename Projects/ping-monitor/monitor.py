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

last_status = None
while True:
    response = os.system(f"ping -n 1 {target} > nul")
    current_status = "UP" if response == 0 else "DOWN"

    if current_status != last_status:
       print(f"{target} is {current_status}")
       log(f"{target} is {current_status}")
       last_status = current_status

    time.sleep(2)
