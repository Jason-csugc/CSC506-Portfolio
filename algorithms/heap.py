# heap.py

def heap(arr, n, i):
    lar = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[lar]:
        lar = l
    if r < n and arr[r] > arr[lar]:
        lar = r
    if lar != i:
        arr[i], arr[lar] = arr[lar], arr[i]
        heap(arr, n, lar)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heap(arr, n, i)
    for i in range(n - 1, 0 , -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap(arr, i, 0)
