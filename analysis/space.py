import tracemalloc

def space_function(func, arr):
    arr_copy = arr.copy()
    tracemalloc.start()
    func(arr_copy)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return peak