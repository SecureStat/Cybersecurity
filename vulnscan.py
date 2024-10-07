import subprocess
import re

def scan_network(network):
    print(f"Scanning network {network}...")
    # Run Nmap quick scan on the network
    result = subprocess.run(['nmap', '-sn', network], capture_output=True, text=True)
    return result.stdout

def parse_nmap_output(output):
    # Extract IP addresses and hostnames from Nmap output
    hosts = re.findall(r'Nmap scan report for ([\d.]+)\n.*?(\(.*?\))?\n', output, re.DOTALL)
    device_info = []
    for host in hosts:
        ip = host[0]
        hostname = host[1].strip('()') if host[1] else 'Unknown'
        device_info.append((ip, hostname))
    return device_info

def guess_device_type(ip):
    # Guess device type based on IP (this is a very basic placeholder)
    # You might want to enhance this logic based on actual scans or additional information
    if ip.startswith("192.168.1"):
        return "Local Device (e.g., PC, Printer)"
    elif ip.startswith("192.168.0"):
        return "Another Local Device (e.g., Router)"
    else:
        return "Unknown Device Type"

def main():
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
