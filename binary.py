def left_bound(A:list, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:   # A[middle] >= key
            right = middle
    return left

    def right_bound(A:list, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:   # A[middle] > key
            right = middle
    return right
