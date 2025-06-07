from algorithms import bubble, merge
import random
import tkinter as tk
from analysis import timer
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def run_analysis():
    sizes = [100, 500, 1000, 2000]
    algorithms = {
        'Bubble Sort': bubble.bubble_sort,
        'Merge Sort': merge.merge_sort
        }

    results = []
    for size in sizes:
        for name, func in algorithms.items():
            for run in range(2):
                arr = random.sample(range(size * 10), size)
                exec_time = timer.time_function(func, arr)
                results.append({'Algorithm': name, 'Size': size, 'Time (s)': exec_time})

    df = pd.DataFrame(results)
    display_results(df)

def display_results(df, frame, textbox): #TODO: update code to generate tk info and manage frame and textbox
    fig, ax = plt.subplots(figsize=(6, 4))
    avg_df = df.groupby(['Algorithm', 'Size']).mean().reset_index()
    for alg in avg_df['Algorithm'].unique():
        data = avg_df[avg_df['Algorithm'] == alg]
        ax.plot(data['Size'], data['Time (s)'], label=alg, marker='o')
    ax.set_title("Sorting Time Complexity")
    ax.set_xlabel("Input Size")
    ax.set_ylabel("Time (s)")
    ax.legend()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    table_data = avg_df.pivot(index='Size', columns='Algorithm', values='Time (s)').round(6)

    complexity_map = {
        "Bubble Sort": "O(n²)",
        "Merge Sort": "O(n log n)"
    }

    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, "Average Execution Time Table (in seconds):\n\n")
    textbox.insert(tk.END, table_data.to_string())
    textbox.insert(tk.END, "\n\nTheoretical Time Complexities:\n")
    for alg, comp in complexity_map.items():
        textbox.insert(tk.END, f"{alg}: {comp}\n")
