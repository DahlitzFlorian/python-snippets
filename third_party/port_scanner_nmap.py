"""Reference: https://medium.com/ediblesec/5-python-libraries-for-cyber-security-8f34f5f1e3b8
Hint: Make sure, that you have Nmap installed on your OS"""
import nmap

nm = nmap.PortScanner()
nm.scan("127.0.0.1", "22-443")

for host in nm.all_hosts():
    print("----------------------------------------------------")
    print(f"Host : {host} ({nm[host].hostname()})")
    print(f"State : {nm[host].state()}")

    for protocol in nm[host].all_protocols():
        print("----------")
        print(f"Protocol : {protocol}")
        port_list = sorted(nm[host][protocol].keys())

        for port in port_list:
            print(f"port : {port}\tstate : {nm[host][protocol][port]['state']}")
