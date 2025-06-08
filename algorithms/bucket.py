from algorithms import insertion

# def bucket_sort(arr):
#     n = len(arr)
#     buckets = [[] for _ in range(n)]
#     for num in arr:
#         bi = int(n * num)
#         buckets[bi].append(num)
#     for bucket in buckets:
#         insertion.insertion_sort(bucket)        
#     index = 0
#     for bucket in buckets:
#         for num in bucket:
#             arr[index] = num
#             index += 1

def bucket_sort(arr):
    # 1. Create empty buckets
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]

    # 2. Distribute elements into buckets
    max_val = max(arr)
    for num in arr:
        index = int(num * num_buckets / (max_val + 1))
        buckets[index].append(num)

    # 3. Sort each bucket
    for bucket in buckets:
        insertion.insertion_sort(bucket)

    # 4. Concatenate buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr