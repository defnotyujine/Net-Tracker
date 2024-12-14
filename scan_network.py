import subprocess

def scan_network():
    print("\n[ Network Scanner - Using Nmap ]")
    target = input("Enter the target IP Address or range (e.g., 192.168.1.1/24): ")
    
    if not target:
        print("[-] No target specified. Returning to main menu.")
        return

    try:
        print("\n[!] Scanning... Please wait.")
        result = subprocess.run(
            ["nmap", "-sn", target],
            capture_output=True,
            text=True,
        )
        raw_output = result.stdout

        hosts = []
        current_host = {}
        for line in raw_output.splitlines():
            if line.startswith("Nmap scan report for"):
                parts = line.replace("Nmap scan report for", "").strip()
                if " " in parts:
                    hostname, ip = parts.rsplit(" ", 1)
                else:
                    hostname, ip = "N/A", parts
                current_host = {"IP": ip, "Hostname": hostname}
                hosts.append(current_host)
            elif line.startswith("MAC Address"):
                mac = line.split()[2]
                manufacturer = " ".join(line.split()[3:])
                if current_host:
                    current_host["MAC"] = mac
                    current_host["Manufacturer"] = manufacturer

        hosts.sort(key=lambda x: x["IP"])

        print("\n{:<20} {:<20} {:<20} {:<30}".format("IP Address", "Hostname", "MAC Address", "Manufacturer"))
        print("=" * 90)
        for host in hosts:
            print("{:<20} {:<20} {:<20} {:<30}".format(
                host["IP"], host["Hostname"], host.get("MAC", "N/A"), host.get("Manufacturer", "N/A")
            ))

    except Exception as e:
        print(f"[-] Error during network scan: {e}")
