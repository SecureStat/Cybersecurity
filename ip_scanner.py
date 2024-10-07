"""
ip_scanner.py: Network Scanning and Vulnerability Detection Script

This script scans a specified network, identifies devices on the network, 
and optionally runs a vulnerability scan (nmap --script vuln) on a selected device.

Usage:
    python nip_scanner.py

You will be prompted to enter the network range (e.g., 192.168.1.0/24) and 
then select a device to run the vulnerability scan on.

Dependencies:
    - Nmap (You must have Nmap installed on your system and accessible via the command line)
    - Python subprocess and re modules

Legal Disclaimer:
This script is for educational purposes only. Unauthorized scanning or exploitation of 
networks or devices is illegal and unethical. Ensure you have explicit permission from 
the network's owner before running any scans. The author assumes no responsibility for 
any misuse of this tool. Use it responsibly and comply with all relevant laws.

Author: Colin
"""

import subprocess
import re

def scan_network(network):
    """
    Scans the specified network using Nmap's ping scan (-sn).
    
    Parameters:
        network (str): The network range to scan (e.g., 192.168.1.0/24)
    
    Returns:
        str: The raw output from the Nmap scan.
    """
    print(f"Scanning network {network}...")
    # Run Nmap quick scan on the network
    result = subprocess.run(['nmap', '-sn', network], capture_output=True, text=True)
    return result.stdout

def parse_nmap_output(output):
    """
    Parses the Nmap output to extract IP addresses and hostnames.

    Parameters:
        output (str): The raw Nmap output.

    Returns:
        list of tuples: A list of (IP, hostname) tuples for each device found.
    """
    # Extract IP addresses and hostnames from Nmap output
    hosts = re.findall(r'Nmap scan report for ([\d.]+)\n.*?(\(.*?\))?\n', output, re.DOTALL)
    device_info = []
    for host in hosts:
        ip = host[0]
        hostname = host[1].strip('()') if host[1] else 'Unknown'
        device_info.append((ip, hostname))
    return device_info

def guess_device_type(ip):
    """
    Guesses the device type based on the IP address.
    
    Parameters:
        ip (str): The IP address of the device.
    
    Returns:
        str: A string indicating the likely device type.
    """
    # Guess device type based on IP (this is a very basic placeholder)
    if ip.startswith("192.168.1"):
        return "Local Device (e.g., PC, Printer)"
    elif ip.startswith("192.168.0"):
        return "Another Local Device (e.g., Router)"
    else:
        return "Unknown Device Type"

def main():
    """
    Main function to scan the network, display devices, and optionally run a vulnerability scan.
    
    Prompts the user for the network range and allows selection of a device to scan.
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
