# NOVA: Intelligent Adaptive Operating System Resource Management Framework

**NOVA** is a Python-based operating system resource management framework that simulates CPU scheduling algorithms, evaluates process scheduling performance, and monitors real-time host-system resources.

The project explores how adaptive scheduling strategies can improve process management by adjusting CPU time allocation based on ready-queue conditions.

## Project Overview

Traditional CPU scheduling algorithms use predefined rules to determine how processes receive CPU time. NOVA implements several scheduling strategies and introduces **NOVA Adaptive Round Robin (NARR)**, a rule-based approach that dynamically adjusts the time quantum based on the number of processes waiting in the ready queue.

NOVA also includes a resource monitoring component that collects CPU and memory information from the host operating system using Python's `psutil` library.

The framework combines scheduling simulation, performance analysis, workload experimentation, and system resource monitoring in one application.

## Key Features

- **Multiple CPU Scheduling Algorithms:** Implements FCFS, Shortest Job First (SJF), Priority Scheduling, and Round Robin.
- **Adaptive Scheduling:** Introduces NOVA Adaptive Round Robin (NARR), which adjusts the time quantum based on ready-queue length.
- **Process Management:** Represents processes with attributes including process ID, arrival time, burst time, priority, and scheduling metrics.
- **Performance Analysis:** Calculates average waiting time, turnaround time, response time, throughput, and simulated CPU utilization.
- **Workload Simulation:** Tests scheduling algorithms against CPU-intensive, short-process, and mixed workloads.
- **System Resource Monitoring:** Uses `psutil` to collect host CPU usage, memory utilization, CPU core count, and running process count.
- **Interactive Dashboard:** Provides a Streamlit interface for exploring scheduling results and resource information.

## System Architecture

NOVA is organized into modular components:

| Component | Responsibility |
|---|---|
| Process Manager | Defines and manages simulated process attributes |
| CPU Scheduling Engine | Executes traditional scheduling algorithms |
| Adaptive Scheduling Engine | Implements dynamic time-quantum adjustment |
| Workload Manager | Provides different process workload configurations |
| Resource Monitor | Collects host-system CPU and memory information |
| Performance Analyzer | Calculates and compares scheduling metrics |
| Streamlit Dashboard | Presents project functionality and results through an interactive interface |

## Scheduling Algorithms

NOVA implements five scheduling strategies:

1. **First Come, First Served (FCFS):** Executes processes in order of arrival.
2. **Shortest Job First (SJF):** Selects the available process with the shortest burst time.
3. **Priority Scheduling:** Selects the available process with the highest scheduling priority.
4. **Round Robin (RR):** Allocates CPU time using a fixed time quantum.
5. **NOVA Adaptive Round Robin (NARR):** Dynamically adjusts the time quantum according to the number of processes waiting in the ready queue.

### NOVA Adaptive Round Robin

NARR uses a queue-based heuristic to adjust the time quantum.

The adjustment is calculated using:

\[
Q_t = \min\left(Q_{\max},\max\left(Q_{\min},
Q_b\left(1+\frac{L_t}{L_r}\right)\right)\right)
\]

Where:

- \(Q_t\): Adjusted time quantum
- \(Q_b\): Baseline time quantum
- \(L_t\): Current ready-queue length
- \(L_r\): Reference queue length
- \(Q_{\min}\): Minimum allowed quantum
- \(Q_{\max}\): Maximum allowed quantum

The implementation rounds the calculated quantum to an integer and applies the configured minimum and maximum limits.

## Experimental Workloads

NOVA evaluates scheduling algorithms using three workload configurations:

- **CPU-Intensive:** Contains processes with larger CPU burst times.
- **Short-Process:** Contains processes with relatively small burst times.
- **Mixed:** Combines processes with different arrival times and CPU burst requirements.

Each algorithm is evaluated against the same workload configurations to support consistent comparisons.

## Performance Metrics

The framework calculates:

- Average Waiting Time
- Average Turnaround Time
- Average Response Time
- Throughput
- Simulated CPU Utilization

The resource monitoring component separately reports actual host-system CPU and memory measurements.

**Important distinction:** Scheduling metrics are calculated from simulated workloads. Host-system resource measurements are collected independently and are not measurements of the simulated scheduler's effect on the operating system.

## Technologies Used

- Python
- Streamlit
- psutil
- Pandas
- NumPy
- Matplotlib
- Git and GitHub

## Project Structure

```text
nova-os-resource-manager/
│
├── analytics/
│   └── performance.py
│
├── monitoring/
│   └── resource_monitor.py
│
├── process_manager/
│   └── process.py
│
├── scheduler/
│   ├── adaptive.py
│   ├── fcfs.py
│   ├── priority.py
│   ├── round_robin.py
│   └── sjf.py
│
├── app.py
├── dashboard.py
├── experiments.py
├── workloads.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/tooflykayy/nova-os-resource-manager.git
```

### 2. Navigate into the project directory

```bash
cd nova-os-resource-manager
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

For macOS and Linux:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Running NOVA

### Run the main scheduling application

```bash
python app.py
```

### View available workloads

```bash
python workloads.py
```

### Run scheduling experiments

```bash
python experiments.py
```

### Launch the interactive dashboard

```bash
streamlit run dashboard.py
```

The Streamlit application will provide a local browser interface for interacting with NOVA.

## Project Goals

NOVA was developed to explore operating system scheduling concepts, compare traditional CPU scheduling strategies, and investigate how adaptive time allocation can respond to changing process workloads.

The project demonstrates modular software design, process scheduling simulation, performance evaluation, system monitoring, and interactive data presentation.

## Future Improvements

Potential future enhancements include:

- Expanding adaptive scheduling strategies.
- Adding additional workload configurations.
- Improving dashboard visualizations.
- Incorporating more detailed resource monitoring.
- Expanding automated testing and performance evaluation.

## Author

**Makayla Waleed**

Graduate Student, Computer Science

**Project:** NOVA — Intelligent Adaptive Operating System Resource Management Framework
