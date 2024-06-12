# search algorithms for lists
import math


def linear_search(arr, x) -> int:
    n = len(arr)
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


def sentinel_search(arr, key):
    n = len(arr)
    last = arr[n - 1]
    arr[n - 1] = key
    i = 0
    while arr[i] != key:
        i += 1
    arr[n - 1] = last
    if (i < n - 1) or (arr[n - 1] == key):
        return i
    else:
        return -1


def meta_binary_search(arr, key):
    n = len(arr)
    lg = int(math.log2(n - 1)) + 1
    pos = 0
    for i in range(lg - 1, -1, -1):
        if arr[pos] == key:
            return pos
        new_pos = pos | (1 << i)
        if ((new_pos < n) and
                (arr[new_pos] <= key)):
            pos = new_pos
    return pos if (arr[pos] == key) else -1


def __interpolation_search(arr, lo, hi, x):
    if lo == hi:
        return lo
    if lo <= hi and arr[lo] <= x <= arr[hi]:
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            return __interpolation_search(arr, pos + 1, hi, x)
        if arr[pos] > x:
            return __interpolation_search(arr, lo, pos - 1, x)
    return -1


def interpolation_search(arr, x):
    n = len(arr)
    return __interpolation_search(arr, 0, n - 1, x)
