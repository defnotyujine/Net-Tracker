import random
import time

def monitor_device_health():
    """
    Simulates Device Health Monitoring by generating mock CPU, memory, and latency stats.
    Replace with real network queries as necessary.
    """
    print("\nStarting Device Health Monitor...")
    time.sleep(1)  
    
    devices = [
        {"device": "Router", "cpu_usage": random.randint(1, 100), "memory_usage": random.randint(1, 100), "latency": random.randint(5, 50)},
        {"device": "Server", "cpu_usage": random.randint(1, 100), "memory_usage": random.randint(1, 100), "latency": random.randint(5, 50)},
        {"device": "IoT Sensor", "cpu_usage": random.randint(1, 100), "memory_usage": random.randint(1, 100), "latency": random.randint(5, 50)}
    ]
    
    print("\nDevice Health Scan Results:")
    for device in devices:
        print(f"Device: {device['device']}")
        print(f"  - CPU Usage: {device['cpu_usage']}%")
        print(f"  - Memory Usage: {device['memory_usage']}%")
        print(f"  - Latency: {device['latency']} ms")
        print("-" * 30)
    
    print("\nScan Complete.\n")
