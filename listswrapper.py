from random import randint
import sortlistings
import searchalgorithms

from enum import Enum


class SortingAlgo(Enum):
    Bubble = 1
    Selection = 2
    Insertion = 3
    Heap = 4
    Merge = 5
    Quick = 6


class SearchAlgo(Enum):
    Linear = 1
    Sentinel = 2
    Binary = 3
    Interpolation = 4


def generate_random_list(length: int, min_value: int, max_value: int) -> list:
    random_list = []
    for i in range(length):
        random_list.append(randint(min_value, max_value))
    return random_list


def sort(arr: list, sort_type: SortingAlgo) -> list:
    match sort_type:
        case SortingAlgo.Bubble:
            return sortlistings.bubble_sort(arr)
        case SortingAlgo.Selection:
            return sortlistings.selection_sort(arr)
        case SortingAlgo.Insertion:
            return sortlistings.insertion_sort(arr)
        case SortingAlgo.Heap:
            return sortlistings.heap_sort(arr)
        case SortingAlgo.Merge:
            return sortlistings.merge_sort(arr)
        case SortingAlgo.Quick:
            return sortlistings.quick_sort(arr)
        case _:
            print("invalid type")
            return arr


def sort_list(arr: list, sort_type: int) -> list:
    if sort_type > SortingAlgo.Quick.value or sort_type < SortingAlgo.Bubble.value:
        print(f"invalid type: {sort_type}")
        return arr
    return sort(arr, SortingAlgo(sort_type))


def arithmetic_mean(arr: list) -> float:
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)


def search(arr: list, value, search_type: SearchAlgo) -> int:
    match search_type:
        case SearchAlgo.Linear:
            return searchalgorithms.linear_search(arr, value)
        case SearchAlgo.Sentinel:
            return searchalgorithms.sentinel_search(arr, value)
        case SearchAlgo.Binary:
            return searchalgorithms.meta_binary_search(arr, value)
        case SearchAlgo.Interpolation:
            return searchalgorithms.interpolation_search(arr, value)
        case _:
            print(f"invalid type: {search_type}")
            return -2


def search_list(arr: list, value, search_type: int) -> int:
    if search_type > SearchAlgo.Interpolation.value or search_type < SearchAlgo.Linear.value:
        print(f"invalid type: {search_type}")
        return -2
    return search(arr, value, SearchAlgo(search_type))
