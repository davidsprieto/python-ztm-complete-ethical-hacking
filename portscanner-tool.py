import socket
import termcolor


def scan(address, ports):
    print(f"\n Starting scan for IP Address: {address}")
    for port in range(1, ports):
        scan_port(address, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+] PORT: {port} OPENED")
        sock.close()
    except:
        pass


user_addresses = input("[*] Enter IP addresses to scan separated by a comma (ex: IP address, IP address): ")
user_ports = int(input("[*] Enter the number of ports you want to scan: "))

if ', ' in user_addresses:
    print(termcolor.colored("[*] Scanning multiple addresses...", "red"))
    for ip in user_addresses.split(', '):
        scan(ip.strip(), user_ports)
else:
    scan(user_addresses, user_ports)

# CODE EXPLANATION:
# This code is a simple port scanner that allows the user to input one or multiple IP addresses and the number of ports they want to scan.
# First, the code imports the necessary modules: `socket` for creating network connections and `termcolor` for colored output.
# Next, there are two functions defined: `scan()` and `scan_port()`.
# The `scan()` function takes two parameters: `address` (the IP address to scan) and `ports` (the number of ports to scan).
# It starts by printing a message indicating the start of the scan for the given IP address. Then, it iterates over a range of numbers from 1 to `ports` (excluding `ports`).
# For each number, it calls the `scan_port()` function passing the IP address and the current port number.
# The `scan_port()` function takes two parameters: `ipaddress` (the IP address to scan) and `port` (the port number to scan).
# Inside the function, it tries to create a socket object and connect to the given IP address and port. If the connection is successful,
# it prints a message indicating that the port is open. Finally, it closes the socket. If any exception occurs during the connection attempt,
# it simply passes and continues to the next port.
# After the function definitions, the code prompts the user to enter the IP addresses they want to scan, separated by a comma. It also asks for the number of ports to scan.
# If the user enters multiple IP addresses (separated by a comma and a space), the code prints a message indicating that it is scanning multiple addresses.
# It then splits the input string by the comma and space, and iterates over the resulting list. For each IP address,
# it calls the `scan()` function passing the address and the number of ports.
# If the user enters only one IP address, the code directly calls the `scan()` function with the entered address and the number of ports.
