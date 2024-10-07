This repository contains various Python scripts designed for cybersecurity tasks, including network scanning, vulnerability scanning, and port enumeration. These tools utilize the Nmap network scanner to gather information about devices on a network, guess device types, and scan for open ports and vulnerabilities.

Tools Included
dnsenum.py: A script for performing slow DNS enumeration scans on a target host.
vulnscan.py: A tool to scan a network for connected devices and run Nmap vulnerability scans on them.
sitescan.py: A script that performs gradual port scans on a target host and outputs the results to a CSV file.
Installation
Prerequisites
Python 3.6 or later
Nmap (Network Mapper)
Python Package Installation
First, clone the repository:

bash
Copy code
git clone https://github.com/SecureStat/Cybersecurity.git
cd Cybersecurity
Then, install the required Python dependencies using pip:

bash
Copy code
pip install python-nmap
Installing Nmap
Ensure that Nmap is installed on your system. You can install it via:

Ubuntu/Debian:
bash
Copy code
sudo apt install nmap
macOS (using Homebrew):
bash
Copy code
brew install nmap
Windows: Download the installer from the Nmap official site.
Usage
1. DNS Enumeration (dnsenum.py)
This tool performs a slow DNS enumeration scan on a target host.

bash
Copy code
python dnsenum.py
When prompted, enter the target host (e.g., example.com).

2. Vulnerability Scanner (vulnscan.py)
This script scans a network for connected devices and allows you to perform an Nmap vulnerability scan on a selected device.

bash
Copy code
python vulnscan.py
When prompted, enter the network range (e.g., 192.168.1.0/24).

3. Gradual Port Scanner (gradual_scan.py)
This tool performs a gradual port scan on a target host and writes the results to a CSV file.

bash
Copy code
python gradual_scan.py
When prompted, enter the target website (e.g., example.com) and the port range to scan (e.g., 65535).

Legal Disclaimer
Author: Colin

These tools are provided for educational and ethical hacking purposes only. Unauthorized use of these scripts against systems or networks that you do not have permission to test is illegal and punishable by law. The author is not responsible for any misuse or damages caused by these scripts.

Always ensure you have explicit permission before running these tools on any network or system.
