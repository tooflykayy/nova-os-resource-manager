
from dataclasses import dataclass


@dataclass
class Process:
    """Represents a process in the NOVA scheduling simulator."""

    pid: int
    arrival_time: int
    burst_time: int
    priority: int = 1

    start_time: int = 0
    completion_time: int = 0
    waiting_time: int = 0
    turnaround_time: int = 0
    response_time: int = 0
    remaining_time: int = 0

    def __post_init__(self):
        if self.pid < 1:
            raise ValueError("Process ID must be positive.")
        if self.arrival_time < 0:
            raise ValueError("Arrival time cannot be negative.")
        if self.burst_time <= 0:
            raise ValueError("Burst time must be positive.")

        self.remaining_time = self.burst_time

    def reset(self):
        """Reset runtime values before another scheduling experiment."""
        self.start_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = 0
        self.remaining_time = self.burst_time
