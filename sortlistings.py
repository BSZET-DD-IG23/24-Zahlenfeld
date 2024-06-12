# sort_functions.py

from typing import List
from heapq import heappop, heappush


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble Sort: Repeatedly steps through the list, compares adjacent elements and swaps them
                    if they are in the wrong order.
    :rtype: None
    :param arr:
    """
    new_arr = arr[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if new_arr[j] > new_arr[j + 1]:
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
    return new_arr


def selection_sort(arr: List[int]) -> List[int]:
    """
    Selection Sort: Divides the list into a sorted and an unsorted region.
                    It repeatedly finds the minimum element from the unsorted region and moves it to the sorted region.
    :rtype: None
    :param arr:
    """
    new_arr = arr[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if new_arr[j] < new_arr[min_idx]:
                min_idx = j
        new_arr[i], new_arr[min_idx] = new_arr[min_idx], new_arr[i]
    return new_arr


def insertion_sort(arr):
    n = len(arr)  # Get the length of the array
    new_arr = arr[:]

    if n <= 1:
        return new_arr  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = new_arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < new_arr[j]:  # Move elements greater than key one position ahead
            new_arr[j + 1] = new_arr[j]  # Shift elements to the right
            j -= 1
        new_arr[j + 1] = key  # Insert the key in the correct position
    return new_arr


def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort: Chooses a 'pivot' element from the list and partitions the other elements into two sub-arrays
    according to whether they are less than or greater than the pivot. It then recursively sorts the sub-arrays.
    :return:
    :rtype: List[int]
    :param arr:
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


def merge_sort(arr):
    # Base case: if the length of the array is 1 or less, it is already sorted
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # Divide the array into two halves: left_half and right_half
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive calls to merge_sort for sorting the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted left and right halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []  # List to store the merged result
    i = j = 0  # Pointers for iterating through the left and right halves

    # Compare elements from the left and right halves and add them to the result list in the correct order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left half to the result list
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from the right half to the result list
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)
    ordered = []
    while heap:
        ordered.append(heappop(heap))
    return ordered
