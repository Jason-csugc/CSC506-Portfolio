from algorithms import bubble, bucket, heap, insertion, merge, quick
import random
from analysis import timer
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

    results = []
    for size in sizes:
        for name, func in algorithms.items():
            for run in range(10):
                arr = random.sample(range(size * 10), size)
                exec_time = timer.time_function(func, arr)
                results.append({'Algorithm': name, 'Size': size, 'Time (s)': exec_time})

    df = pd.DataFrame(results)
    return df
