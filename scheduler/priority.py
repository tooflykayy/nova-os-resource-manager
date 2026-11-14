
from copy import deepcopy


def schedule_priority(processes):
    """Non-preemptive Priority Scheduling.
    
    Lower priority number means higher priority.
    """

    remaining = deepcopy(processes)
    completed = []
    current_time = 0

    while remaining:

        available = [
            p for p in remaining
            if p.arrival_time <= current_time
        ]

        if not available:
            current_time = min(
                p.arrival_time for p in remaining
            )
            continue

        # Select the highest-priority available process.
        process = min(
            available,
            key=lambda p: (p.priority, p.arrival_time, p.pid)
        )

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
        remaining.remove(process)

    return completed
