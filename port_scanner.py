import subprocess


def port_scan():
    print("\n[ Port Scanner - Using Nmap ]")
    target_ip = input("Enter the target IP Address (e.g., 192.168.8.0/24): ")
    if not target_ip:
        print("[-] No target IP specified. Returning to main menu.")
        return

    port_range = input("Enter the port range to scan (e.g., 1-1024): ")
    if not port_range:
        print("[-] No port range specified. Using default range 1-1024.")
        port_range = "1-1024"

    try:
        print("\n[!] Scanning for open ports... Please wait.")
        result = subprocess.run(
            ["nmap", "-p", port_range, target_ip],
            capture_output=True,
            text=True,
        )
        raw_output = result.stdout

        open_ports = []
        for line in raw_output.splitlines():
            if "/tcp" in line and "open" in line:
                open_ports.append(line.strip())

        if open_ports:
            print("\nOpen Ports Found:")
            print("=" * 30)
            for port in open_ports:
                print(port)
        else:
            print("\nNo open ports detected.")

    except Exception as e:
        print(f"[-] Error during port scan: {e}")
