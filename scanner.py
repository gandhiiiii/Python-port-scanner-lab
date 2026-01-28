import socket

target_ip = "127.0.0.1"
ports = [21, 22, 80, 443]

print ("Starting scan...\n)

for port in ports:
	s = socket.socket(socket.AF_INET, socket.SOC_STREAM)
	s.settimeout(1)

	result = s.connect_ex((target_ip, port))

	if result == 0;
		print(f"[+] Port {port} is OPEN"]
	else:
		print(f"[-] Port {port} is closed")
	s.close()

print("\nScan complete.")
