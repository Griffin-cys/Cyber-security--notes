import socket

target = input("Enter website/IP (e.g., scanme.nmap.org): ")

ports = [21, 22, 80, 443, 3306, 8080]

print(f"\nScanning {target}...\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN ✅")
    else:
        print(f"Port {port} is CLOSED ❌")
    s.close()

print("\nScan Done!")
