import unittest
import sortlistings
import listswrapper
import searchalgorithms
from random import randint


def create_unique_list():
    test_list = listswrapper.generate_random_list(10, 0, 100)
    sorted_list = sorted(test_list)
    while test_list == sorted_list:
        test_list = listswrapper.generate_random_list(10, 0, 100)
        sorted_list = sorted(test_list)
    print(test_list)
    return test_list


class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
        print("Bubble Sort: ")
        test_list = create_unique_list()
        sorted_list = sorted(test_list)
        test_list = sortlistings.bubble_sort(test_list)
        print(test_list)
        print(sorted_list)
        self.assertEqual(test_list, sorted_list)

    def test_quick_sort(self):
        print("Quick Sort: ")
        test_list = create_unique_list()
        sorted_list = sorted(test_list)

        test_list = sortlistings.quick_sort(test_list)
        print(test_list)
        print(sorted_list)
        self.assertEqual(test_list, sorted_list)

    def test_selection_sort(self):
        print("Selection Sort: ")
        test_list = create_unique_list()
        sorted_list = sorted(test_list)
        test_list = sortlistings.selection_sort(test_list)
        print(test_list)
        print(sorted_list)
        self.assertEqual(test_list, sorted_list)

    def test_merge_sort(self):
        print("Merge Sort: ")
        test_list = create_unique_list()
        sorted_list = sorted(test_list)
        test_list = sortlistings.merge_sort(test_list)
        print(test_list)
        print(sorted_list)
        self.assertEqual(test_list, sorted_list)

    def test_insertion_sort(self):
        print("Insertion Sort: ")
        test_list = create_unique_list()
        sorted_list = sorted(test_list)
        test_list = sortlistings.insertion_sort(test_list)
        print(test_list)
        print(sorted_list)
        self.assertEqual(test_list, sorted_list)

    def test_heap_sort(self):
        print("Heap Sort: ")
        test_list = create_unique_list()
        sorted_list = sorted(test_list)
        test_list = sortlistings.heap_sort(test_list)
        print(test_list)
        print(sorted_list)
        self.assertEqual(test_list, sorted_list)


class TestSearching(unittest.TestCase):
    def test_linear_search(self):
        print("Linear Search: ")
        test_list = create_unique_list()
        index = randint(0, len(test_list) - 1)
        print(index)
        print(test_list[index])
        val = test_list[index]
        idx = searchalgorithms.linear_search(test_list, val)
        print(idx)
        self.assertEqual(idx, index)

    def test_sentinel_search(self):
        print("Sentinel Search: ")
        test_list = create_unique_list()
        index = randint(0, len(test_list) - 1)
        print(index)
        print(test_list[index])
        val = test_list[index]
        idx = searchalgorithms.sentinel_search(test_list, val)
        print(idx)
        self.assertEqual(idx, index)

    def test_binary_search(self):
        print("Meta Binary Search: ")
        test_list = sorted(create_unique_list())
        index = randint(0, len(test_list) - 1)
        print(index)
        print(test_list[index])
        val = test_list[index]
        idx = searchalgorithms.meta_binary_search(test_list, val)
        print(idx)
        self.assertEqual(idx, index)

    def test_interpolation_search(self):
        print("Interpolation Search: ")
        test_list = sorted(create_unique_list())
        index = randint(0, len(test_list) - 1)
        print(index)
        print(test_list[index])
        val = test_list[index]
        idx = searchalgorithms.interpolation_search(test_list, val)
        print(idx)
        self.assertEqual(idx, index)


class TestLists(unittest.TestCase):
    def test_sort_list(self):
        print("Sort List: ")
        test_list = create_unique_list()
        sorted_list = sorted(test_list)

        test_list1 = listswrapper.sort_list(test_list, 1)
        test_list2 = listswrapper.sort_list(test_list, 2)
        test_list3 = listswrapper.sort_list(test_list, 3)
        test_list4 = listswrapper.sort_list(test_list, 4)
        test_list5 = listswrapper.sort_list(test_list, 5)
        test_list6 = listswrapper.sort_list(test_list, 6)
        test_list7 = listswrapper.sort_list(test_list, 7)
        self.assertEqual(test_list1, sorted_list)
        self.assertEqual(test_list2, sorted_list)
        self.assertEqual(test_list3, sorted_list)
        self.assertEqual(test_list4, sorted_list)
        self.assertEqual(test_list5, sorted_list)
        self.assertEqual(test_list6, sorted_list)
        self.assertNotEqual(test_list7, sorted_list)

    def test_search_list(self):
        print("Search List: ")
        test_list = sorted(create_unique_list())
        print(test_list)

        index = randint(0, len(test_list) - 1)
        print(test_list[index])
        print(index)
        val = test_list[index]
        idx1 = listswrapper.search_list(test_list, val, 1)
        print(idx1)
        idx2 = listswrapper.search_list(test_list, val, 2)
        print(idx2)
        idx3 = listswrapper.search_list(test_list, val, 3)
        print(idx3)
        idx4 = listswrapper.search_list(test_list, val, 4)
        print(idx4)
        idx5 = listswrapper.search_list(test_list, val, 5)
        print(idx5)
        self.assertEqual(idx1, index)
        self.assertEqual(idx2, index)
        self.assertEqual(idx3, index)
        self.assertEqual(idx4, index)
        self.assertNotEqual(idx5, index)


if __name__ == '__main__':
    unittest.main()
