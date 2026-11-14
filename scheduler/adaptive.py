
from collections import deque
from copy import deepcopy


def schedule_adaptive(
    processes,
    base_quantum=2,
    min_quantum=1,
    max_quantum=6,
    reference_queue_length=2
):
    """
    NOVA Adaptive Round Robin (NARR).

    Dynamically adjusts the time quantum based on
    the number of processes waiting in the ready queue.
    """

    if base_quantum <= 0:
        raise ValueError("Base quantum must be positive.")

    if min_quantum <= 0 or max_quantum < min_quantum:
        raise ValueError("Invalid quantum limits.")

    if reference_queue_length <= 0:
        raise ValueError("Reference queue length must be positive.")

    remaining = deepcopy(processes)
    remaining.sort(key=lambda p: (p.arrival_time, p.pid))

    ready_queue = deque()
    completed = []

    current_time = 0
    index = 0

    while ready_queue or index < len(remaining):

        # Add processes that have arrived.
        while (
            index < len(remaining)
            and remaining[index].arrival_time <= current_time
        ):
            ready_queue.append(remaining[index])
            index += 1

        # Advance time if no process is ready.
        if not ready_queue:
            current_time = remaining[index].arrival_time
            continue

        process = ready_queue.popleft()

        # Calculate the adaptive quantum using the ready queue length.
        queue_length = len(ready_queue)

        adjusted_quantum = base_quantum * (
            1 + queue_length / reference_queue_length
        )

        quantum = round(adjusted_quantum)

        quantum = max(
            min_quantum,
            min(max_quantum, quantum)
        )

        # Record the first CPU execution.
        if process.remaining_time == process.burst_time:
            process.start_time = current_time
            process.response_time = (
                current_time - process.arrival_time
            )

        # Execute the process.
        execution_time = min(
            quantum,
            process.remaining_time
        )

        current_time += execution_time
        process.remaining_time -= execution_time

        # Add newly arrived processes.
        while (
            index < len(remaining)
            and remaining[index].arrival_time <= current_time
        ):
            ready_queue.append(remaining[index])
            index += 1

        # Check whether the process has completed.
        if process.remaining_time == 0:

            process.completion_time = current_time

            process.turnaround_time = (
                process.completion_time - process.arrival_time
            )

            process.waiting_time = (
                process.turnaround_time - process.burst_time
            )

            completed.append(process)

        else:
            ready_queue.append(process)

    return completed
