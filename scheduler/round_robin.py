
from collections import deque
from copy import deepcopy


def schedule_round_robin(processes, quantum=2):
    """Schedule processes using Round Robin."""

    if quantum <= 0:
        raise ValueError("Time quantum must be positive.")

    remaining = deepcopy(processes)
    remaining.sort(key=lambda p: (p.arrival_time, p.pid))

    ready_queue = deque()
    completed = []

    current_time = 0
    next_process = 0

    while ready_queue or next_process < len(remaining):

        # If the CPU is idle, move to the next arrival.
        if not ready_queue:
            current_time = max(
                current_time,
                remaining[next_process].arrival_time
            )

        # Add all processes that have arrived.
        while (
            next_process < len(remaining)
            and remaining[next_process].arrival_time <= current_time
        ):
            ready_queue.append(remaining[next_process])
            next_process += 1

        process = ready_queue.popleft()

        # Record the first time this process gets CPU time.
        if process.remaining_time == process.burst_time:
            process.start_time = current_time
            process.response_time = (
                current_time - process.arrival_time
            )

        # Run the process for one quantum or until it finishes.
        execution_time = min(quantum, process.remaining_time)

        current_time += execution_time
        process.remaining_time -= execution_time

        # Add newly arrived processes to the queue.
        while (
            next_process < len(remaining)
            and remaining[next_process].arrival_time <= current_time
        ):
            ready_queue.append(remaining[next_process])
            next_process += 1

        if process.remaining_time > 0:
            ready_queue.append(process)
        else:
            process.completion_time = current_time
            process.turnaround_time = (
                process.completion_time - process.arrival_time
            )
            process.waiting_time = (
                process.turnaround_time - process.burst_time
            )

            completed.append(process)

    return completed

