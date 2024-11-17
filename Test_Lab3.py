# test_Lab3.py

import Lab3

def test_bubble_sort_ascending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == test_arr

def test_bubble_sort_descending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert result == test_arr

def test_bubble_sort_large_input():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 45, 33, 76]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 1

def test_bubble_sort_empty():
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 0

def test_bubble_sort_non_integer():
    input_arr = [64, "34", 25, 12, 22, 11, 90]  # Contains a string element
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 2  # Expect 2 for non-integer input

def test_bubble_sort_invalid_order():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    result = Lab3.bubble_sort(input_arr, 3)
    assert result == []  # Expect empty list for invalid order

if __name__ == "__main__":
    print("Running tests...")
    test_bubble_sort_ascending()
    test_bubble_sort_descending()
    test_bubble_sort_large_input()
    test_bubble_sort_empty()
    test_bubble_sort_non_integer()
    test_bubble_sort_invalid_order()
    print("All tests passed.")
