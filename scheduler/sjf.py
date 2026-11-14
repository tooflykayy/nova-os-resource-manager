
from copy import deepcopy


def schedule_sjf(processes):
    """Non-preemptive Shortest Job First scheduling."""

    remaining = deepcopy(processes)
    completed = []
    current_time = 0

    while remaining:

        # Find processes that have arrived.
        available = [
            p for p in remaining
            if p.arrival_time <= current_time
        ]

        # If no process is ready, advance to the next arrival.
        if not available:
            current_time = min(
                p.arrival_time for p in remaining
            )
            continue

        # Select the shortest available burst.
        process = min(
            available,
            key=lambda p: (p.burst_time, p.arrival_time, p.pid)
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
