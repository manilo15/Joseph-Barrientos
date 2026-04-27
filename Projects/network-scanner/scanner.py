import os
import socket

network = "192.168.1." 
count = 0

print("Scanning network...\n")

for i in range(1, 255):
    ip = network + str(i)
    response = os.system(f"ping -n 1 -w 100 {ip} > nul")

    if response == 0:
        count += 1
        
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = "No hostname found"

        print(f"{ip:<16} | {hostname}")

print(f"\nActive devices found: {count}")