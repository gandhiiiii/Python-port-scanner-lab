# Python-port-scanner-lab

## Overview
This project showcases a simple TCP port scanner written in Python using the socket library. The scanner was tested in a two-VM virtualBox homelab to simulate basic network reconnaissance

## Lab Setup
-Hypervisor: Oracle VirtualBox
-Scanner VML Ubuntu Linux
-Target VM: Ubuntu Linux
-Network Type: Internal Network
-IP Addressing:
  -Scanner VM: 192.168.100.20
  -Target VM: 192.168.100.10

## Target Configuration
-OpenSSH Server installed and running
-SSH listening on port 22

## Scanner Logic
The scanner performs a TCP connect scan by attempting to establish a socket connection to each port.
  -If the connection succeeds, the port is marked OPEN
  -If it fails, the port is marked CLOSED

##Example Output
  [+]Port 22 is OPEN
  [-]Port 23 is CLOSED
  [-]Port 24 is CLOSED

## Security Takeaways
-Open ports reveal exposed services
-TCP connect scans rely on the full TCP handshake
-Network isolation and segmentation affect scan visibility

## Future Improvements
-Add banner grabbing
-Add port range input
-Add multi-threading
  
