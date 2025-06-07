import time

def time_function(func, arr):
    start = time.perf_counter()
    func(arr.copy())
    return time.perf_counter() - start