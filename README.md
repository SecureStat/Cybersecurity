Network Scanning and Vulnerability Assessment Tools
This repository contains a collection of Python scripts designed for network scanning and vulnerability assessment:

dnsenum.py: Performs a slow Nmap scan on a specified target host to potentially avoid detection.
ip_scanner.py: Scans a specified network, identifies devices, and allows for an optional vulnerability scan using nmap --script vuln.
sitescan.py: Conducts a gradual Nmap port scan on a target website, saving results to a CSV file.
vulnscan.py: Scans a local network for devices and allows you to select one for a vulnerability scan using nmap --script vuln.

Installation (Debian based instructions). In terminal, you will need to run
git clone https://github.com/SecureStat/Cybersecurity
pip install nmap
python dnsenum.py

You can replace "dnsenum.py" with any of the other files.

Legal Disclaimer
These scripts are for educational purposes only. Unauthorized scanning or probing of networks or devices is illegal and unethical. Always obtain explicit permission from the owner of the target network or device before running any scans. The author takes no responsibility for any misuse of these tools. Use them responsibly and in compliance with all applicable laws.

