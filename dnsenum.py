import nmap

def slow_scan(target_host):
  """Performs a slow Nmap scan on the specified target host."""

  scanner = nmap.PortScanner()
  scanner.scan(host=target_host, ports='1-1000', timing_template="S", min_parallelism=1, max_parallelism=1)  # Adjust port range and timing template as needed

  print(scanner.scaninfo())
  print(scanner[target_host].all())

if __name__ == "__main__":
  target_host = input("Enter the target host: ")
  slow_scan(target_host)
