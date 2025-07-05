# amalyzer.py

from algorithms import bubble, bucket, heap, insertion, merge, quick
import random
from analysis import timer, space
import pandas as pd

def run_analysis():
    sizes = [100, 500, 1000, 2000]
    algorithms = {
        'Bubble Sort': bubble.bubble_sort,
        'Bucket Sort': bucket.bucket_sort,
        'Heap Sort': heap.heap_sort,
        'Insertion Sort': insertion.insertion_sort,
        'Merge Sort': merge.merge_sort,
        'Quick Sort': quick.quick_sort
        }

    time_results = []
    space_results = []
    for size in sizes:
        for name, func in algorithms.items():
            for _ in range(5):
                arr = random.sample(range(size * 10), size)
                exec_time = timer.time_function(func, arr.copy())
                space_used = space.space_function(func, arr.copy())
                time_results.append({'Algorithm': name, 'Size': size, 'Time (s)': exec_time})
                space_results.append({'Algorithm': name, 'Size': size, 'Space (bytes)': space_used})

    time_df = pd.DataFrame(time_results)
    space_df = pd.DataFrame(space_results)
    return time_df, space_df
