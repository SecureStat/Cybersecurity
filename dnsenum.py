"""
dnsenum.py: Slow Nmap Scan Script

This script is used to perform a slow Nmap scan on the specified target host.
It scans the first 1000 ports (by default) using the slowest timing template 
to avoid detection in certain situations. 

Note: Ensure you have permission to scan the target host before using this tool.

Usage:
    python dnsenum.py

You will be prompted to enter the target host (e.g., an IP address or domain name).

Dependencies:
    - nmap (You must have the Nmap package and its Python bindings installed.)

Legal Disclaimer:
This script is for educational purposes only. You must have explicit permission 
from the target system's owner to conduct any network scan. Unauthorized network 
scanning is illegal and can lead to severe consequences. Use this tool responsibly.

Author: Colin
"""

import nmap

def slow_scan(target_host):
    """
    Performs a slow Nmap scan on the specified target host.
    
    Parameters:
        target_host (str): The IP address or domain name of the host to scan.
    
    Returns:
        None
    """
    scanner = nmap.PortScanner()

    # Scanning the first 1000 ports with slow timing to avoid detection
    # Adjust timing_template, ports, and parallelism as needed for your use case
    scanner.scan(
        host=target_host, 
        ports='1-1000', 
        arguments='-T1 --min-parallelism 1 --max-parallelism 1'
    )
    
    # Print scan info and results
    print(scanner.scaninfo())
    print(scanner[target_host].all())

if __name__ == "__main__":
    # Ask the user for the target host (e.g., IP address or domain)
    target_host = input("Enter the target host: ")
    slow_scan(target_host)
