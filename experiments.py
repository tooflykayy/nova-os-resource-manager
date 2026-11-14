
from workloads import get_workload

from scheduler.fcfs import schedule_fcfs
from scheduler.sjf import schedule_sjf
from scheduler.priority import schedule_priority
from scheduler.round_robin import schedule_round_robin
from scheduler.adaptive import schedule_adaptive

from analytics.performance import (
    analyze_performance,
    display_performance
)


def run_experiments():
    """Compare all scheduling algorithms across three workloads."""

    algorithms = {
        "FCFS": schedule_fcfs,
        "SJF": schedule_sjf,
        "Priority": schedule_priority,
        "Round Robin": schedule_round_robin,
        "NOVA NARR": schedule_adaptive
    }

    workload_types = [
        "CPU-intensive",
        "Short-process",
        "Mixed"
    ]

    print("\n")
    print("=" * 75)
    print("NOVA - SCHEDULING EXPERIMENTS")
    print("=" * 75)

    for workload_name in workload_types:

        print(f"\nWORKLOAD: {workload_name}")
        print("=" * 75)

        # Get the same original workload for each algorithm.
        original_processes = get_workload(workload_name)

        results = {}

        for algorithm_name, algorithm_function in algorithms.items():

            # Each algorithm receives a fresh copy of the workload.
            processes = get_workload(workload_name)

            if algorithm_name == "Round Robin":
                scheduled = algorithm_function(
                    processes,
                    quantum=2
                )
            else:
                scheduled = algorithm_function(processes)

            results[algorithm_name] = scheduled

        # Calculate and display performance metrics.
        performance = analyze_performance(results)
        display_performance(performance)


if __name__ == "__main__":
    run_experiments()
