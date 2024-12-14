import scan_network
import port_scanner
from vulnerability_scan import vulnerability_scan  # Importing the vulnerability scanner function
from device_health_monitor import monitor_device_health  # Import the new device health monitor module
from network_traffic_analysis import analyze_network_traffic  # Import the network traffic analysis module
from intrusion_detection import start_ids
from colorama import Fore, Style, init

init(autoreset=True)

ascii_art = r"""
###  ##  ### ###  #### ##                #### ##  ### ##     ##      ## ##   ##  ###  ### ###  ### ##            
  ## ##   ##  ##  # ## ##                # ## ##   ##  ##     ##    ##   ##  ##  ##    ##  ##   ##  ##           
 # ## #   ##        ##         ####        ##      ##  ##   ## ##   ##       ## ##     ##       ##  ##           
 ## ##    ## ##     ##         ####        ##      ## ##    ##  ##  ##       ## ##     ## ##    ## ##            
 ##  ##   ##        ##         ####        ##      ## ##    ## ###  ##       ## ###    ##       ## ##            
 ##  ##   ##  ##    ##                     ##      ##  ##   ##  ##  ##   ##  ##  ##    ##  ##   ##  ##           
###  ##  ### ###   ####                   ####    #### ##  ###  ##   ## ##   ##  ###  ### ###  #### ##    
"""

def menu():

    while True:

        print("\n" + Fore.RED + ascii_art + Style.RESET_ALL)  # Color the ASCII art red
        print("======================================================================================================")
        print(Fore.RED + "                       NET-TRACKER - Developed by VVolf and SassyScorp" + Style.RESET_ALL)
        print("======================================================================================================")
        print("1. Scan Network")
        print("2. Port Scanning")
        print("3. Vulnerability Scanner")
        print("4. Device Health Monitor")
        print("5. Network Traffic Analysis")
        print("6. Intrusion Detection System")
        print("7. Exit")
        print("===========================================")

        choice = input("Enter your choice (1/2/3/4/5/6): ")
        
        if choice == '1':
            scan_network.scan_network()
        elif choice == '2':
            port_scanner.port_scan()
        elif choice == '3':
            vulnerability_scan()
        elif choice == '4':
            monitor_device_health()
        elif choice == '5':
            analyze_network_traffic()
        elif choice == '6':
            start_ids()
        elif choice == '7':
            print("\nThank you for using NET-TRACKER! Goodbye.")
            break
        else:
            print("\n[!] Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()
