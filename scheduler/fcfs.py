
from copy import deepcopy


def schedule_fcfs(processes):
    """Schedule processes using First Come, First Served."""

    # Work with copies so the original workload remains unchanged.
    scheduled = deepcopy(processes)

    # Sort by arrival time, then process ID.
    scheduled.sort(key=lambda p: (p.arrival_time, p.pid))

    current_time = 0
    completed = []

    for process in scheduled:

        # Wait if the CPU is idle.
        if current_time < process.arrival_time:
            current_time = process.arrival_time

        process.start_time = current_time
        process.response_time = (
            process.start_time - process.arrival_time
        )

        current_time += process.burst_time

        process.completion_time = current_time
        process.turnaround_time = (
            process.completion_time - process.arrival_time
        )
        process.waiting_time = (
            process.turnaround_time - process.burst_time
        )

        process.remaining_time = 0

        completed.append(process)

    return completed
