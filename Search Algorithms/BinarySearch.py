import math
import unittest


def binary_search(b_list, value):
    mid = int(math.floor(len(b_list) / 2))

    if b_list[mid] == value:
        return True
    elif len(b_list) == 1:  # Make sure this is the second case
        return False
    elif b_list[mid] < value:
        return binary_search(b_list[mid:], value)
    elif b_list[mid] > value:
        return binary_search(b_list[:mid], value)


def infinite_array(array, value, index=0):
    """
        Find value x if it exists in an infinite array. The first n values will be sorted,
        the rest denoted with i. We do not know the value of -9999. Return -1 if value does not exist
        O log(p) where p is the position

        This is a divide and conquer algorithm
    """
    array_value = array[index]
    if value == array_value:
        return True
    elif array_value > value or array_value == -9999:
        return binary_search(array[:index], value)
    else:
        index = 1 if index == 0 else index
        return infinite_array(array, value, index=index * 2)


class Tests(unittest.TestCase):
    inf = [1, 3, 5, 6, 7, 7, 8, 10, 11, 14, 15, 21, 25, 27, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999,
           -9999, -9999, -9999 - 9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999 - 9999,
           -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999 - 9999, -9999, -9999, -9999, -9999,
           -9999, -9999, -9999, -9999, -9999, -9999 - 9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999,
           -9999, -9999 - 9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999 - 9999, -9999,
           -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999 - 9999, -9999, -9999, -9999, -9999, -9999,
           -9999, -9999, -9999, -9999, -9999 - 9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999,
           -9999 - 9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999 - 9999, -9999, -9999,
           -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999]

    def test_binary_search(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 3))
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 2))
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 5))
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 9))

    def test_infinite_array(self):
        self.assertTrue(infinite_array(self.inf, 3))
        self.assertTrue(infinite_array(self.inf, 5))
        self.assertFalse(infinite_array(self.inf, 58))


if __name__ == '__main__':
    unittest.main()
