import nmap
import time
import csv

def gradual_port_scan(target_host, port_range):
  """Performs a gradual Nmap scan on the specified target host and port range."""

  scanner = nmap.PortScanner()
  step_size = 100  # Adjust step size as needed
  start_time = time.time()

  with open("scan_results.csv", "w", newline="") as csvfile:
    fieldnames = ["Port", "State", "Service"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for start_port in range(1, port_range + 1, step_size):
      end_port = min(start_port + step_size - 1, port_range)
      scanner.scan(host=target_host, ports=f"{start_port}-{end_port}", timing_template="S")

      # Write results to CSV
      for port in scanner[target_host]['tcp'].keys():
        writer.writerow({
          "Port": port,
          "State": scanner[target_host]['tcp'][port]['state'],
          "Service": scanner[target_host]['tcp'][port]['name']
        })

      # Print progress and estimated remaining time
      elapsed_time = time.time() - start_time
      total_ports = port_range
      scanned_ports = start_port + step_size - 1
      remaining_ports = total_ports - scanned_ports
      estimated_remaining_time = elapsed_time * remaining_ports / scanned_ports
      print(f"Scanned {scanned_ports}/{total_ports} ports. Estimated remaining time: {estimated_remaining_time:.2f} seconds")

      # Add a delay between scans to avoid overwhelming the target
      time.sleep(1)  # Adjust delay as needed

if __name__ == "__main__":
  target_website = input("Enter the target website URL: ")
  port_range = int(input("Enter the maximum port to scan (e.g., 65535): "))

  # Extract the domain from the URL
  target_host = target_website.split("//")[-1].split("/")[0]

  gradual_port_scan(target_host, port_range)
