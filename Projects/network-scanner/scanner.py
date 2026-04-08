import os
import socket

network = "192.168.1."  # Modify as needed. 

print("Scanning network...\n")

for i in range(1, 255):
    ip = network + str(i)
    response = os.system(f"ping -n 1 -w 100 {ip} > nul")

    if response == 0:
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = "Unknown"

        print(f"{ip} is up - {hostname}")
