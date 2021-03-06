import unittest

from admin.sorting.models_sort import Sorting

class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        instance = Sorting()
        instance.random_arr = [9,8,7,6,5,4,3,2,1]
        arr = instance.bubble_sort()
        print(f'{arr}')
        self.assertEqual(arr,[1,2,3,4,5,6,7,8,9])

    def test_merge_sort(self):
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        arr1 = Sorting.merge_sort(arr)
        self.assertEqual(arr1, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_quick_sort(self):
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        arr = Sorting.quick_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])
