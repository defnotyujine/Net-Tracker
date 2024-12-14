from scapy.all import sniff
import time

ip_activity = {}

SCAN_THRESHOLD = 10  
TIME_WINDOW = 60 

def monitor_packet(packet):
    """
    Monitor packets in real-time and check for potential intrusion patterns.
    """
    try:
        if packet.haslayer('IP'):
            src_ip = packet['IP'].src

            current_time = time.time()
            if src_ip in ip_activity:
                ip_activity[src_ip] = [
                    t for t in ip_activity[src_ip] if current_time - t < TIME_WINDOW
                ]
                
                ip_activity[src_ip].append(current_time)

                if len(ip_activity[src_ip]) > SCAN_THRESHOLD:
                    print(f"[!] Potential port scan detected from IP: {src_ip}")
                    print(f"[!] Number of attempts: {len(ip_activity[src_ip])}")
                    ip_activity[src_ip] = []
            else:
                ip_activity[src_ip] = [current_time]
    except Exception as e:
        print(f"Error processing packet: {e}")

def start_ids():
    """
    Start the IDS by sniffing packets.
    """
    print("[*] Starting Intrusion Detection System...")
    sniff(prn=monitor_packet, store=0) 

if __name__ == "__main__":
    start_ids()
