import sys
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from analysis import analyzer


class Display():
    def __init__(self):
        self.Textbox = None
        self.Frame = None
        self.Root = None
        self.Button = None
        self._df = None

        self.Root = tk.Tk()
        self.Root.title("Sorting Algorithm Analyzer")

        self.Frame = tk.Frame(self.Root)
        self.Frame.pack(padx=10, pady=10)

        self.Button = tk.Button(self.Root, text="Run Analysis", command=self.analyze)
        self.Button.pack(pady=10)

        self.Textbox = tk.Text(self.Root, height=12, width=80)
        self.Textbox.pack(padx=10, pady=10)

        self.Root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.Root.mainloop()
             

    def on_closing(self):
                print("Window is closing")
                self.Root.destroy()
                sys.exit()

    def Display_results(self): 
        fig, ax = plt.subplots(figsize=(6, 4))
        avg_df = self._df.groupby(['Algorithm', 'Size']).mean().reset_index()
        for alg in avg_df['Algorithm'].unique():
            data = avg_df[avg_df['Algorithm'] == alg]
            ax.plot(data['Size'], data['Time (s)'], label=alg, marker='o')
        ax.set_title("Sorting Time Complexity")
        ax.set_xlabel("Input Size")
        ax.set_ylabel("Time (s)")
        ax.legend()
        canvas = FigureCanvasTkAgg(fig, master=self.Frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        table_data = avg_df.pivot(index='Size', columns='Algorithm', values='Time (s)').round(6)

        complexity_map = {
            "Bubble Sort": "O(n²)",
            "Bucket Sort": "O(n log n)",
            "Heap Sort": "O(n log n)",
            "Insertion Sort": "O(n²)",
            "Merge Sort": "O(n log n)",
            "Quick Sort": "O(n²)"
        }

        self.Textbox.delete("1.0", tk.END)
        self.Textbox.insert(tk.END, "Average Execution Time Table (in seconds):\n\n")
        self.Textbox.insert(tk.END, table_data.to_string())
        self.Textbox.insert(tk.END, "\n\nTheoretical Time Complexities:\n")
        for alg, comp in complexity_map.items():
            self.Textbox.insert(tk.END, f"{alg}: {comp}\n")
    
    def analyze(self):
         self._df = analyzer.run_analysis()
         self.Display_results()
