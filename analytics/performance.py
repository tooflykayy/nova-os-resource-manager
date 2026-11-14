
def analyze_performance(results_by_algorithm):
    """
    Compare CPU scheduling algorithms using performance metrics.

    Metrics:
    - Average waiting time
    - Average turnaround time
    - Average response time
    - Throughput
    - Simulated CPU utilization
    """

    if not results_by_algorithm:
        raise ValueError("No scheduling results were provided.")

    performance = {}

    for algorithm, processes in results_by_algorithm.items():

        if not processes:
            raise ValueError(
                f"No processes found for {algorithm}."
            )

        total_processes = len(processes)

        average_waiting = (
            sum(p.waiting_time for p in processes)
            / total_processes
        )

        average_turnaround = (
            sum(p.turnaround_time for p in processes)
            / total_processes
        )

        average_response = (
            sum(p.response_time for p in processes)
            / total_processes
        )

        total_burst_time = sum(
            p.burst_time for p in processes
        )

        first_arrival = min(
            p.arrival_time for p in processes
        )

        final_completion = max(
            p.completion_time for p in processes
        )

        total_elapsed_time = final_completion - first_arrival

        throughput = (
            total_processes / total_elapsed_time
            if total_elapsed_time > 0 else 0
        )

        cpu_utilization = (
            total_burst_time / total_elapsed_time * 100
            if total_elapsed_time > 0 else 0
        )

        performance[algorithm] = {
            "average_waiting": average_waiting,
            "average_turnaround": average_turnaround,
            "average_response": average_response,
            "throughput": throughput,
            "cpu_utilization": cpu_utilization
        }

    return performance


def display_performance(performance):
    """Display a comparison of all scheduling algorithms."""

    print("\n")
    print("=" * 100)
    print("NOVA PERFORMANCE ANALYZER")
    print("=" * 100)

    print(
        f"{'Algorithm':<30}"
        f"{'Avg Wait':<14}"
        f"{'Avg Turnaround':<18}"
        f"{'Avg Response':<16}"
        f"{'Throughput':<14}"
        f"{'CPU Usage':<12}"
    )

    print("-" * 100)

    for algorithm, metrics in performance.items():

        print(
            f"{algorithm:<30}"
            f"{metrics['average_waiting']:<14.2f}"
            f"{metrics['average_turnaround']:<18.2f}"
            f"{metrics['average_response']:<16.2f}"
            f"{metrics['throughput']:<14.2f}"
            f"{metrics['cpu_utilization']:<12.2f}%"
        )

    print("-" * 100)

    # Lower values are better for waiting, turnaround,
    # and response time.
    best_waiting = min(
        performance,
        key=lambda a: performance[a]["average_waiting"]
    )

    best_turnaround = min(
        performance,
        key=lambda a: performance[a]["average_turnaround"]
    )

    best_response = min(
        performance,
        key=lambda a: performance[a]["average_response"]
    )

    # Higher values are better for throughput and utilization.
    best_throughput = max(
        performance,
        key=lambda a: performance[a]["throughput"]
    )

    best_cpu = max(
        performance,
        key=lambda a: performance[a]["cpu_utilization"]
    )

    print("\nPERFORMANCE HIGHLIGHTS")
    print("-" * 100)

    print(f"Lowest Average Waiting Time: {best_waiting}")
    print(f"Lowest Average Turnaround Time: {best_turnaround}")
    print(f"Lowest Average Response Time: {best_response}")
    print(f"Highest Throughput: {best_throughput}")
    print(f"Highest Simulated CPU Utilization: {best_cpu}")

    print("=" * 100)
