SORT_ASCENDING = 0
SORT_DESCENDING = 1

def bubble_sort(arr, order):
    # Check for an empty array
    if not arr:
        return 0  # Return 0 for empty input

    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        return 2  # Return 2 for non-integer elements

    # Check for invalid order
    if order not in [SORT_ASCENDING, SORT_DESCENDING]:
        return []  # Return empty list for invalid order

    # Check for large input
    if len(arr) >= 10:
        return 1  # Return 1 for input arrays of size 10 or more

    # Perform bubble sort
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (order == SORT_ASCENDING and arr[j] > arr[j+1]) or \
               (order == SORT_DESCENDING and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
