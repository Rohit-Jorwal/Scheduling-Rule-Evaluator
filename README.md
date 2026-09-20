# Scheduling-Rule-Evaluator
Python-based scheduling rule evaluator with Tkinter GUI and Matplotlib visualization.
This a Python-based project for evaluating and comparing different job-sequencing rules in a single-machine scheduling environment.

## ⚙️ Key Features

* Implements six scheduling rules:

  * FCFS (First Come, First Served)
  * SPT (Shortest Processing Time)
  * LPT (Longest Processing Time)
  * Minimum Slack
  * Least Criticality Ratio
  * Random Rule
* Generates processing times and due dates for jobs
* Calculates scheduling performance measures
* Provides an interactive GUI for entering job-related inputs
* Supports custom job ordering for the Random Rule
* Generates graphs for comparing scheduling rules

## 📊 Performance Measures

The project calculates:

* Average Lateness
* Average Flow Time
* Utilization
* Average Jobs in System

## 🖥️ GUI

The graphical interface is developed using **Tkinter** and allows the user to:

* Enter the number of jobs
* Select processing-time cases
* Select due-date cases
* Calculate performance measures
* View the calculated results
* View graphical comparisons

## 📈 Visualization

**Matplotlib** is used to generate bar charts comparing the scheduling rules based on:

* Average Lateness
* Average Flow Time
* Utilization

## 🛠️ Technologies & Libraries

* Python
* Tkinter
* Matplotlib
* Random

## 🔄 Working Process

```text
User Input
    ↓
Generate Job Data
    ↓
Apply Scheduling Rules
    ↓
Calculate Performance Measures
    ↓
Display Results
    ↓
Generate Comparison Graphs
```

## 🎯 Objective

The objective of this project is to provide an interactive tool for evaluating different scheduling rules and comparing their performance using numerical results and graphical visualization.
