from scapy.all import sniff


def packet_callback(packet):
    """
    Callback function to process packets during sniffing.
    Logs source, destination, and packet summary information.
    """
    try:
        print(f"Packet Captured: {packet.summary()}")
        if packet.haslayer("IP"):  
            print(f"Source IP: {packet["IP"].src}")
            print(f"Destination IP: {packet["IP"].dst}")
        if packet.haslayer("TCP"): 
            print(f"Source Port: {packet["TCP"].sport}")
            print(f"Destination Port: {packet["TCP"].dport}")
        print("-" * 50)
    except Exception as e:
        print(f"Error processing packet: {e}")


def analyze_network_traffic():
    """
    Function to initialize and monitor live network traffic using scapy.
    Runs live capture for a specific number of packets or time.
    """
    print("\n[+] Starting Network Traffic Analysis...")
    print("[+] Press Ctrl+C to stop at any time.\n")

    try:
        sniff(prn=packet_callback, filter="ip", store=0) 
    except KeyboardInterrupt:
        print("\n[!] Network Traffic Analysis Stopped by User.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("\n[+] Network Traffic Analysis Terminated.")
