def is_min_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < n and arr[i] > arr[left_child]:
            return 0
        if right_child < n and arr[i] > arr[right_child]:
            return 0
            
    return 1
arr = list(map(int, input().split()))
print(is_min_heap(arr)) 
