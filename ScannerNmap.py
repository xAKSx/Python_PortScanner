import nmap
import pyfiglet
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER BY AKS")
print(ascii_banner)

scanner = nmap.PortScanner()

target = input("Enter the IP address to scan: ")

options = '-p 1-1000'
print("_" * 50)
print("scanning Started at: " + str(datetime.now()))
print("_" * 50)

scanner.scan(target, arguments=options)

for host in scanner.all_hosts():
    if scanner[host].state() == 'up':
        print('Host: %s' % host)
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                print('Port: %s/%s' % (port, proto))
