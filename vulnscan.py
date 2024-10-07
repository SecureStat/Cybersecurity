"""
vulnscan.py: Network Vulnerability Scanning Script

This script scans a local network for devices and allows the user to select a device to run 
an Nmap vulnerability scan using the `--script vuln` option. The script outputs the scanned 
devices and their IP addresses and provides a basic guess of the device type based on the IP.

Usage:
    python vulnscan.py

You will be prompted to enter the network range to scan (e.g., 192.168.1.0/24) and select a 
device for the vulnerability scan.

Dependencies:
    - Nmap (Ensure Nmap is installed and accessible from your system)
    - Python re and subprocess modules

Legal Disclaimer:
This script is intended for educational purposes only. Unauthorized scanning or probing of networks 
or devices is illegal and unethical. Ensure that you have explicit permission from the owner of 
the target network or device before running any scans. The author takes no responsibility for any misuse 
of this tool. Always use it responsibly and in compliance with all applicable laws.

Author: Colin
"""

import subprocess
import re

def scan_network(network):
    """
    Scans the specified network using Nmap's ping scan (-sn).

    Parameters:
        network (str): The network to scan (e.g., 192.168.1.0/24).

    Returns:
        str: The raw Nmap output.
    """
    print(f"Scanning network {network}...")
    result = subprocess.run(['nmap', '-sn', network], capture_output=True, text=True)
    return result.stdout

def parse_nmap_output(output):
    """
    Parses Nmap output to extract IP addresses and hostnames.

    Parameters:
        output (str): The raw Nmap output.

    Returns:
        list of tuples: A list of tuples containing IP and hostname information.
    """
    hosts = re.findall(r'Nmap scan report for ([\d.]+)\n.*?(\(.*?\))?\n', output, re.DOTALL)
    device_info = []
    for host in hosts:
        ip = host[0]
        hostname = host[1].strip('()') if host[1] else 'Unknown'
        device_info.append((ip, hostname))
    return device_info

def guess_device_type(ip):
    """
    Provides a basic guess of the device type based on its IP address.

    Parameters:
        ip (str): The IP address of the device.

    Returns:
        str: A guess of the device type.
    """
    if ip.startswith("192.168.1"):
        return "Local Device (e.g., PC, Printer)"
    elif ip.startswith("192.168.0"):
        return "Another Local Device (e.g., Router)"
    else:
        return "Unknown Device Type"

def main():
    """
    Main function to scan the network and run the Nmap vulnerability scan on a selected device.
    """
    # Get network to scan
    network = input("Enter network (e.g., 192.168.1.0/24): ")

    # Scan the network
    output = scan_network(network)

    # Parse Nmap output
    device_info = parse_nmap_output(output)

    # Display devices
    print("\nDevices found on the network:")
    for idx, (ip, hostname) in enumerate(device_info):
        device_type = guess_device_type(ip)
        print(f"{idx + 1}. IP: {ip}, Hostname: {hostname}, Type: {device_type}")

    # Ask user which device to run nmap --script vuln on
    choice = int(input("\nEnter the number of the device you want to run nmap --script vuln on: ")) - 1
    if 0 <= choice < len(device_info):
        target_ip = device_info[choice][0]
        print(f"Running nmap --script vuln on {target_ip}...")
        subprocess.run(['nmap', '--script', 'vuln', target_ip])
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
