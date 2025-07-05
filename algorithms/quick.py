# quick.py

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        sort(arr, low, p - 1)
        sort(arr, p + 1, high)
def quick_sort(arr):
    sort(arr, 0, len(arr) - 1)
