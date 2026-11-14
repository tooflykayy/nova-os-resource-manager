
from process_manager.process import Process

from scheduler.fcfs import schedule_fcfs
from scheduler.sjf import schedule_sjf
from scheduler.priority import schedule_priority
from scheduler.round_robin import schedule_round_robin
from scheduler.adaptive import schedule_adaptive

from analytics.performance import (
    analyze_performance,
    display_performance
)

from monitoring.resource_monitor import (
    get_system_resources,
    display_system_resources
)


def display_results(name, results):
    """Display individual scheduling results."""

    print(f"\nAlgorithm: {name}")
    print("-" * 90)

    print(
        f"{'PID':<10}"
        f"{'Arrival':<12}"
        f"{'Burst':<10}"
        f"{'Priority':<10}"
        f"{'Start':<10}"
        f"{'Complete':<12}"
        f"{'Waiting':<10}"
        f"{'Turnaround':<12}"
    )

    print("-" * 90)

    for p in results:
        print(
            f"{p.pid:<10}"
            f"{p.arrival_time:<12}"
            f"{p.burst_time:<10}"
            f"{p.priority:<10}"
            f"{p.start_time:<10}"
            f"{p.completion_time:<12}"
            f"{p.waiting_time:<10}"
            f"{p.turnaround_time:<12}"
        )

    average_waiting = sum(p.waiting_time for p in results) / len(results)
    average_turnaround = sum(p.turnaround_time for p in results) / len(results)
    average_response = sum(p.response_time for p in results) / len(results)

    print(f"\nAverage Waiting Time: {average_waiting:.2f}")
    print(f"Average Turnaround Time: {average_turnaround:.2f}")
    print(f"Average Response Time: {average_response:.2f}")


def main():
    """Run NOVA scheduling, performance, and resource monitoring."""

    # Define the workload used by all scheduling algorithms.
    processes = [
        Process(pid=1, arrival_time=0, burst_time=5, priority=2),
        Process(pid=2, arrival_time=1, burst_time=3, priority=1),
        Process(pid=3, arrival_time=2, burst_time=2, priority=3),
    ]

    print("\nNOVA - CPU Scheduling Engine")
    print("============================")
    print("Scheduling Algorithms Performance Comparison")

    # 1. First Come, First Served
    fcfs_results = schedule_fcfs(processes)

    # 2. Shortest Job First
    sjf_results = schedule_sjf(processes)

    # 3. Priority Scheduling
    priority_results = schedule_priority(processes)

    # 4. Standard Round Robin
    rr_results = schedule_round_robin(
        processes,
        quantum=2
    )

    # 5. NOVA Adaptive Round Robin
    adaptive_results = schedule_adaptive(
        processes,
        base_quantum=2,
        min_quantum=1,
        max_quantum=6,
        reference_queue_length=2
    )

    # Display individual scheduling results.
    display_results(
        "First Come, First Served (FCFS)",
        fcfs_results
    )

    display_results(
        "Shortest Job First (SJF)",
        sjf_results
    )

    display_results(
        "Priority Scheduling",
        priority_results
    )

    display_results(
        "Round Robin (Quantum = 2)",
        rr_results
    )

    display_results(
        "NOVA Adaptive Round Robin (NARR)",
        adaptive_results
    )

    # Organize results for performance analysis.
    results_by_algorithm = {
        "FCFS": fcfs_results,
        "SJF": sjf_results,
        "Priority": priority_results,
        "Round Robin": rr_results,
        "NOVA NARR": adaptive_results
    }

    # Run the Performance Analyzer.
    performance = analyze_performance(
        results_by_algorithm
    )

    display_performance(performance)

    # Monitor actual host computer resources.
    system_resources = get_system_resources()

    display_system_resources(system_resources)


if __name__ == "__main__":
    main()
