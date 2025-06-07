import tkinter as tk
from analyzer import run_analysis
import sys


def on_closing():
            print("Window is closing")
            root.destroy()
            sys.exit()

root = tk.Tk()
root.title("Sorting Algorithm Analyzer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

btn = tk.Button(root, text="Run Analysis", command=run_analysis)
btn.pack(pady=10)

text_box = tk.Text(root, height=12, width=80)
text_box.pack(padx=10, pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()