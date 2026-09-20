import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_measures(rule, processing_times, due_dates, user_order=None):
    n = len(processing_times)
    sorted_jobs = list(range(n))

    if rule == "FCFS":
        pass  
    elif rule == "SPT":
        sorted_jobs.sort(key=lambda x: processing_times[x])
    elif rule == "LPT":
        sorted_jobs.sort(key=lambda x: -processing_times[x])
    elif rule == "SS":
        sorted_jobs.sort(key=lambda x: due_dates[x] - processing_times[x])
    elif rule == "SCR":
        sorted_jobs.sort(key=lambda x: due_dates[x] / processing_times[x])
    elif rule == "Random":
        if user_order:
            sorted_jobs = user_order
        else:
            random.shuffle(sorted_jobs)

    flow_time = 0
    lateness_sum = 0
    cumulative_flow_time = 0
    sorted_processing_times = []
    sorted_due_dates = []
    for job in sorted_jobs:
        sorted_processing_times.append(processing_times[job])
        sorted_due_dates.append(due_dates[job])
        flow_time += processing_times[job]
        cumulative_flow_time += flow_time
        lateness = max(0, flow_time - due_dates[job])
        lateness_sum += lateness

    avg_lateness = lateness_sum / n
    avg_flow_time = cumulative_flow_time / n
    utilization = 100 * sum(processing_times) / cumulative_flow_time
    avg_jobs_in_system = cumulative_flow_time / sum(processing_times)
    
    return avg_lateness, avg_flow_time, utilization, avg_jobs_in_system, sorted_processing_times, sorted_due_dates

def get_user_order(n):
    user_order_str = simpledialog.askstring("Input", f"Enter the order of job indices (0-{n-1}) separated by commas for the Random rule:")
    if user_order_str:
        try:
            user_order = list(map(int, user_order_str.split(',')))
            if all(0 <= i < n for i in user_order):
                return user_order
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Invalid order format. Please enter indices within the valid range (0 to n-1).")
    else:
        messagebox.showerror("Input Error", "Invalid order format.")
    return None

def plot_results(results, graph_frame):
    rules = list(results.keys())
    avg_lateness = [results[rule]["avg_lateness"] for rule in rules]
    avg_flow_time = [results[rule]["avg_flow_time"] for rule in rules]
    utilization = [results[rule]["utilization"] for rule in rules]

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    axs[0].bar(rules, avg_lateness, color="skyblue")
    axs[0].set_title("Average Lateness")
    axs[0].set_xlabel("Rules")
    axs[0].set_ylabel("Average Lateness")
    axs[1].bar(rules, avg_flow_time, color="skyblue")
    axs[1].set_title("Average Flow Time")
    axs[1].set_xlabel("Rules")
    axs[1].set_ylabel("Average Flow Time")
    axs[2].bar(rules, utilization, color="skyblue")
    axs[2].set_title("Utilization")
    axs[2].set_xlabel("Rules")
    axs[2].set_ylabel("Utilization (%)")

    for widget in graph_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def display_results():
    try:
        num_jobs = int(entry_num_jobs.get())
        proc_case = int(entry_proc_case.get())
        due_case = int(entry_due_case.get())

        if num_jobs <= 0:
            messagebox.showerror("Input Error", "The number of jobs must be greater than 0.")
            return
        if proc_case not in [1, 2, 3] or due_case not in [1, 2]:
            messagebox.showerror("Input Error", "Processing Time Case must be 1-3 and Due Date Case must be 1-2.")
            return
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
        return

    processing_times = [random.randint(2, 100) if proc_case == 3 else random.randint(2, 50) for _ in range(num_jobs)]
    total_proc_time = sum(processing_times)
    due_dates = [int(random.uniform(0.5, 1.1) * total_proc_time) if due_case == 2 else int(random.uniform(0.3, 0.9) * total_proc_time) for _ in range(num_jobs)]

    rules = ["FCFS", "SPT", "LPT", "SS", "SCR", "Random"]
    results = {}

    for rule in rules:
        user_order = None
        if rule == "Random":
            user_order = get_user_order(num_jobs)
            if user_order is None:
                return  
        avg_lateness, avg_flow_time, utilization, avg_jobs_in_system, sorted_processing_times, sorted_due_dates = calculate_measures(rule, processing_times, due_dates, user_order)
        results[rule] = {
            "avg_lateness": avg_lateness,
            "avg_flow_time": avg_flow_time,
            "utilization": utilization,
            "avg_jobs_in_system": avg_jobs_in_system,
            "sorted_processing_times": sorted_processing_times,
            "sorted_due_dates": sorted_due_dates
        }

    output_text.delete(1.0, tk.END)
    for rule, metrics in results.items():
        output_text.insert(tk.END, f"Rule: {rule}\n")
        output_text.insert(tk.END, f"Processing Times (Ordered): {metrics['sorted_processing_times']}\n")
        output_text.insert(tk.END, f"Due Dates (Ordered): {metrics['sorted_due_dates']}\n")
        output_text.insert(tk.END, f"Average Lateness: {metrics['avg_lateness']:.2f}\n")
        output_text.insert(tk.END, f"Average Flow Time: {metrics['avg_flow_time']:.2f}\n")
        output_text.insert(tk.END, f"Utilization: {metrics['utilization']:.2f}%\n\n")

    plot_results(results, graph_frame)

window = tk.Tk()
window.title("Job Scheduling Performance Measures")

# Configure fullscreen on maximize
window.state("zoomed")

top_frame = tk.Frame(window)
top_frame.pack(pady=10)

tk.Label(top_frame, text="Enter Number of Jobs:").grid(row=0, column=0)
entry_num_jobs = tk.Entry(top_frame)
entry_num_jobs.grid(row=0, column=1)
tk.Label(top_frame, text="Select Processing Time Case (1-3):").grid(row=1, column=0)
entry_proc_case = tk.Entry(top_frame)
entry_proc_case.grid(row=1, column=1)
tk.Label(top_frame, text="Select Due Date Case (1-2):").grid(row=2, column=0)
entry_due_case = tk.Entry(top_frame)
entry_due_case.grid(row=2, column=1)

calc_button = tk.Button(top_frame, text="Calculate Performance Measures", command=display_results)
calc_button.grid(row=3, columnspan=2, pady=10)

# Output and Graph Frame setup
main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True)

output_text = tk.Text(main_frame, height=20, width=80)
output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

graph_frame = tk.Frame(main_frame)
graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

window.mainloop()
