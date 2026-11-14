
import streamlit as st
import pandas as pd

from workloads import get_workload

from scheduler.fcfs import schedule_fcfs
from scheduler.sjf import schedule_sjf
from scheduler.priority import schedule_priority
from scheduler.round_robin import schedule_round_robin
from scheduler.adaptive import schedule_adaptive

from analytics.performance import analyze_performance
from monitoring.resource_monitor import get_system_resources


st.set_page_config(
    page_title="NOVA Resource Manager",
    page_icon="⚙️",
    layout="wide"
)

st.title("NOVA")
st.subheader("Intelligent Adaptive Operating System Resource Management")
st.markdown(
    "Compare CPU scheduling algorithms across different process workloads."
)

st.divider()

# Workload selection
st.sidebar.header("Experiment Settings")

workload_name = st.sidebar.selectbox(
    "Select Workload",
    ["CPU-intensive", "Short-process", "Mixed"]
)

quantum = st.sidebar.slider(
    "Round Robin Time Quantum",
    min_value=1,
    max_value=10,
    value=2
)

# Load selected workload
processes = get_workload(workload_name)

st.header(f"{workload_name} Workload")

process_data = [
    {
        "PID": p.pid,
        "Arrival Time": p.arrival_time,
        "Burst Time": p.burst_time,
        "Priority": p.priority
    }
    for p in processes
]

st.dataframe(
    pd.DataFrame(process_data),
    use_container_width=True,
    hide_index=True
)

# Run scheduling algorithms
algorithms = {
    "FCFS": schedule_fcfs,
    "SJF": schedule_sjf,
    "Priority": schedule_priority,
    "Round Robin": lambda p: schedule_round_robin(p, quantum=quantum),
    "NOVA NARR": schedule_adaptive
}

results = {}

for name, algorithm in algorithms.items():
    results[name] = algorithm(get_workload(workload_name))

performance = analyze_performance(results)

# Prepare performance data
rows = []

for algorithm, metrics in performance.items():
    rows.append({
        "Algorithm": algorithm,
        "Average Waiting Time": round(metrics["average_waiting"], 2),
        "Average Turnaround Time": round(metrics["average_turnaround"], 2),
        "Average Response Time": round(metrics["average_response"], 2),
        "Throughput": round(metrics["throughput"], 2),
        "CPU Utilization (%)": round(metrics["cpu_utilization"], 2)
    })

performance_df = pd.DataFrame(rows)

st.divider()
st.header("Scheduling Performance Comparison")

st.dataframe(
    performance_df,
    use_container_width=True,
    hide_index=True
)

# Performance charts
st.subheader("Average Waiting Time")
st.bar_chart(
    performance_df.set_index("Algorithm")[["Average Waiting Time"]]
)

st.subheader("Average Turnaround Time")
st.bar_chart(
    performance_df.set_index("Algorithm")[["Average Turnaround Time"]]
)

st.subheader("Average Response Time")
st.bar_chart(
    performance_df.set_index("Algorithm")[["Average Response Time"]]
)

# Host system monitoring
st.divider()
st.header("Live Host System Monitoring")

st.caption(
    "These measurements describe the computer running NOVA, "
    "not the simulated scheduling workload."
)

if st.button("Refresh System Resources"):
    st.session_state["resources"] = get_system_resources()

if "resources" not in st.session_state:
    st.session_state["resources"] = get_system_resources()

resources = st.session_state["resources"]

col1, col2, col3 = st.columns(3)

col1.metric("CPU Usage", f"{resources['cpu_usage']}%")
col2.metric("Memory Usage", f"{resources['memory_usage']}%")
col3.metric("Running Processes", resources["running_processes"])

col4, col5, col6 = st.columns(3)

col4.metric("CPU Cores", resources["cpu_cores"])
col5.metric("Total Memory", f"{resources['total_memory_gb']} GB")
col6.metric("Available Memory", f"{resources['available_memory_gb']} GB")

st.caption(
    f"Last updated: {resources['timestamp']} | "
    f"Operating System: {resources['operating_system']}"
)

st.divider()
st.caption("NOVA | Advanced Operating Systems Project | 2026")

