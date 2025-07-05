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
        self._df_time = None
        self._df_space = None

        self.Root = tk.Tk()
        self.Root.title("Sorting Algorithm Analyzer")
        self.Root.geometry("750x800")

        self.Root.grid_rowconfigure(0, weight=1)
        self.Root.grid_columnconfigure(0, weight=1)

        self.Frame = tk.Frame(self.Root)
        self.Frame.grid(row=0, column=0, sticky="nsew")

        self.Frame.grid_rowconfigure(0, weight=1)
        self.Frame.grid_columnconfigure(0, weight=1)

        self.Button = tk.Button(self.Root, text="Run Analysis", command=self.analyze)
        self.Button.grid(row=1, column=0, sticky="nsew")

        self.Textbox = tk.Text(self.Root, padx=10, pady=10)
        self.Textbox.grid(row=2, column=0, sticky="nsew")

        self.Root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.Root.mainloop()
             

    def on_closing(self):
                print("Window is closing")
                self.Root.destroy()
                sys.exit()

    def Display_results(self): 
        time_fig, ax = plt.subplots(figsize=(6, 4))
        avg_time_df = self._df_time.groupby(['Algorithm', 'Size']).mean().reset_index()
        for alg in avg_time_df['Algorithm'].unique():
            data = avg_time_df[avg_time_df['Algorithm'] == alg]
            ax.plot(data['Size'], data['Time (s)'], label=alg, marker='o')
        ax.set_title("Sorting Time Complexity")
        ax.set_xlabel("Input Size")
        ax.set_ylabel("Time (s)")
        ax.legend()
        canvas = FigureCanvasTkAgg(time_fig, master=self.Frame)
        canvas.draw()
        canvas_widget_time = canvas.get_tk_widget()
        canvas_widget_time.grid(row=0, column=0, sticky="nsew")

        time_table_data = avg_time_df.pivot(index='Size', columns='Algorithm', values='Time (s)').round(6)

        space_fig, s_ax = plt.subplots(figsize=(6, 4))
        avg_space_df = self._df_space.groupby(['Algorithm', 'Size']).mean().reset_index()
        for s_alg in avg_space_df['Algorithm'].unique():
            s_data = avg_space_df[avg_space_df['Algorithm'] == s_alg]
            s_ax.plot(s_data['Size'], s_data['Space (bytes)'], label=s_alg, marker='o')
        s_ax.set_title("Sorting Space Complexity")
        s_ax.set_xlabel("Input Size")
        s_ax.set_ylabel("Space (bytes)")
        s_ax.legend()
        canvas = FigureCanvasTkAgg(space_fig, master=self.Frame)
        canvas.draw()
        canvas_widget_space = canvas.get_tk_widget()
        canvas_widget_space.grid(row=1, column=0, sticky="nsew")

        space_table_data = avg_space_df.pivot(index='Size', columns='Algorithm', values='Space (bytes)').round(6)

        #TODO: Combine these tables into a dataframe and display as a single table
        time_complexities = {
            "Bubble Sort": "O(n²)",
            "Bucket Sort": "O(n log n)",
            "Heap Sort": "O(n log n)",
            "Insertion Sort": "O(n²)",
            "Merge Sort": "O(n log n)",
            "Quick Sort": "O(n log n)"
        }

        space_complexities = {
            "Bubble Sort": "O(1)",
            "Bucket Sort": "O(n + k)",
            "Heap Sort": "O(1)",
            "Insertion Sort": "O(1)",
            "Merge Sort": "O(n)",
            "Quick Sort": "O(log n)"
        }

        self.Textbox.delete("1.0", tk.END)
        self.Textbox.insert(tk.END, "Average Execution Time Table (in seconds):\n\n")
        self.Textbox.insert(tk.END, time_table_data.to_string())
        self.Textbox.insert(tk.END, "\n\nTheoretical Time Complexities:\n")
        for alg, comp in time_complexities.items():
            self.Textbox.insert(tk.END, f"{alg}: {comp}\n")
        self.Textbox.insert(tk.END, "\n")
        self.Textbox.insert(tk.END, "Average Execution Space Table (in bytes):\n\n")
        self.Textbox.insert(tk.END, space_table_data.to_string())
        self.Textbox.insert(tk.END, "\n\nTheoretical Space Complexities:\n")
        for alg, comp in space_complexities.items():
            self.Textbox.insert(tk.END, f"{alg}: {comp}\n")

        
    
    def analyze(self):
         self._df_time, self._df_space = analyzer.run_analysis()
         self.Display_results()
