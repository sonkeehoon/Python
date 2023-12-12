def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        
        mid = (left+right) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
    return mid