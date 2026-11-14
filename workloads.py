
from process_manager.process import Process


def get_workload(workload_type):
    """
    Return a predefined workload for NOVA testing.
    Each workload uses the same process data
    across all scheduling algorithms.
    """

    if workload_type == "CPU-intensive":
        return [
            Process(1, 0, 12, 2),
            Process(2, 1, 15, 1),
            Process(3, 2, 10, 3),
            Process(4, 3, 18, 2),
            Process(5, 4, 14, 1),
        ]

    elif workload_type == "Short-process":
        return [
            Process(1, 0, 2, 2),
            Process(2, 1, 1, 1),
            Process(3, 2, 3, 3),
            Process(4, 3, 2, 2),
            Process(5, 4, 1, 1),
            Process(6, 5, 2, 3),
        ]

    elif workload_type == "Mixed":
        return [
            Process(1, 0, 8, 2),
            Process(2, 1, 3, 1),
            Process(3, 3, 12, 3),
            Process(4, 4, 2, 2),
            Process(5, 6, 7, 1),
            Process(6, 8, 4, 3),
        ]

    else:
        raise ValueError(
            "Unknown workload type. Choose CPU-intensive, "
            "Short-process, or Mixed."
        )


if __name__ == "__main__":
    for workload_name in [
        "CPU-intensive",
        "Short-process",
        "Mixed"
    ]:
        processes = get_workload(workload_name)

        print(f"\n{workload_name} Workload")
        print("-" * 40)

        for process in processes:
            print(
                f"PID: {process.pid}, "
                f"Arrival: {process.arrival_time}, "
                f"Burst: {process.burst_time}, "
                f"Priority: {process.priority}"
            )
