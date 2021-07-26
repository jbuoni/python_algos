import unittest
import math


def find_min_recursive(array, n, calulated_sum, total_sum):
    if n == 0:
        return abs((total_sum - calulated_sum) - calulated_sum)

    return min(find_min_recursive(array, n - 1, calulated_sum + array[n + 1], total_sum), 
    find_min_recursive(array, n - 1, calulated_sum, total_sum))

def find_min(array):
    length = len(array)
    sum_val = sum(array)
    return find_min_recursive(array, length, 0, sum_val); 



class Test(unittest.TestCase):
    def test_find_min(self):
        min_subsets = find_min([1, 6, 11, 5])
        self.assertEqual(min_subsets, 1)
