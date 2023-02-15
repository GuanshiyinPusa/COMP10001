def binary_search_closest(arr, target):
    low = 0
    high = len(arr) - 1

    closest_match = None
    closest_distance = float('inf')

    while low <= high:
        mid = (low + high) // 2
        if abs(arr[mid] - target) < closest_distance:
            closest_distance = abs(arr[mid] - target)
            closest_match = arr[mid]
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return closest_match


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7.5
print(binary_search_closest(arr, target))
