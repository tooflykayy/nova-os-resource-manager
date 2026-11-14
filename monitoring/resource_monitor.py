
import psutil
import platform
from datetime import datetime


def get_system_resources():
    """
    Collect current system CPU and memory information.
    Uses psutil to monitor the host computer.
    """

    # CPU information
    cpu_usage = psutil.cpu_percent(interval=1)

    cpu_cores = psutil.cpu_count(logical=True)

    # Memory information
    memory = psutil.virtual_memory()

    total_memory = memory.total / (1024 ** 3)
    available_memory = memory.available / (1024 ** 3)
    used_memory = memory.used / (1024 ** 3)

    memory_usage = memory.percent

    # Process information
    running_processes = len(psutil.pids())

    # Collect system information
    resources = {
        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "operating_system": platform.system(),
        "cpu_usage": cpu_usage,
        "cpu_cores": cpu_cores,
        "memory_usage": memory_usage,
        "total_memory_gb": round(total_memory, 2),
        "used_memory_gb": round(used_memory, 2),
        "available_memory_gb": round(available_memory, 2),
        "running_processes": running_processes
    }

    return resources


def display_system_resources(resources):
    """Display collected system resource information."""

    print("\n")
    print("=" * 55)
    print("NOVA SYSTEM RESOURCE MONITOR")
    print("=" * 55)

    print(f"Timestamp: {resources['timestamp']}")
    print(f"Operating System: {resources['operating_system']}")

    print("\nCPU INFORMATION")
    print("-" * 55)
    print(f"CPU Usage: {resources['cpu_usage']}%")
    print(f"Logical CPU Cores: {resources['cpu_cores']}")

    print("\nMEMORY INFORMATION")
    print("-" * 55)
    print(f"Memory Usage: {resources['memory_usage']}%")
    print(f"Total Memory: {resources['total_memory_gb']} GB")
    print(f"Used Memory: {resources['used_memory_gb']} GB")
    print(f"Available Memory: {resources['available_memory_gb']} GB")

    print("\nPROCESS INFORMATION")
    print("-" * 55)
    print(f"Running Processes: {resources['running_processes']}")

    print("=" * 55)
