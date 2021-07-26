import unittest
import numpy
import sys


def kadanes(array):
    """
        Given an array, find the subarray with the max sum
        O(n2)
    :param array:
    :return:
    """
    length = len(array)
    # Use dynamic programming for this. Sorta like the
    # longest palindrome substring
    t = numpy.zeros((length, length))

    max_x = max_j = 0

    for x in range(length):
        for j in range(x, length):
            t[x][j] = t[x][j - 1] + array[j]

            if t[x][j] > t[max_x][max_j]:
                max_j = j
                max_x = x

    return t[max_x][max_j]


def kadanes_v2(array):
    """
        O(n) complexity
    :param array:
    :return:
    """

    answer = - sys.maxint - 1

    t = [answer for i in range(len(array))]
    t[0] = array[0]
    start = end = temp = 0

    for j in range(1, len(array)):
        t[j] = max(t[j - 1], 0) + array[j]

        if t[j] == 0:
            temp = 0

        if t[j] > answer:
            answer = t[j]
            start = temp
            end = j

    # We can return start and end if we want
    return answer


def missing(array):
    """
        Find the missing elements in an array
        assume the array is sorted
        for example 1, 3, 4 is missing 2
    :param array:
    :return:
    """

    missing = []
    length = len(array)

    if length >= 1:
        end = array[length - 1]
        index = length - 2
        while index >= 0:  # We want to go to the second to last character
            next = array[index]

            while next + 1 != end:
                next += 1
                missing.append(next)
            # So confusing a bit but make the new end this index
            end = array[index]
            index -= 1

        return missing


def substring_sum(n):
    length = len(n)

    sum = []
    # Init
    sum.append(int(n[0]))

    result = sum[0]

    for i in range(1, length):
        num_i = int(n[i])
        # Get the current val plus the previous digits
        sum.append((i + 1) * num_i + 10 * sum[i - 1])
        result += sum[i]

    return result


def max_subarray(arr):
    n = len(arr)
    # Sub sequence array
    t = [0 for x in range(n)]

    t[0] = arr[0]

    max_val = -999
    curr_max = arr[0]

    # Sub sequence
    for i in range(1, n):
        # Max will be t[n]
        t[i] = max(t[i - 1] + arr[i], t[i - 1])
        curr_max = max(arr[i], curr_max + arr[i])
        max_val = max(max_val, curr_max)

    max_sub = t[n - 1]
    # Now get single value
    for i in range(n):
        if max_sub < arr[i]:
            max_sub = arr[i]
        if max_val < arr[i]:
            max_val = arr[i]

    return max_val, max_sub


class Test(unittest.TestCase):

    def test_kadanes(self):
        self.assertEqual(kadanes([1, 2, 3, -2, 5]), 9)
        self.assertEqual(kadanes([1, 2, -3, -2, 5]), 5)
        self.assertEqual(kadanes([1, 2, -3, 2, 5]), 7)
        self.assertEqual(kadanes([1, 2, -3, 2, 5]), 7)

    def test_kadanes_v2(self):
        self.assertEqual(kadanes_v2([1, 2, 3, -2, 5]), 9)
        self.assertEqual(kadanes_v2([1, 2, -3, -2, 5]), 5)
        self.assertEqual(kadanes_v2([1, 2, -3, 2, 5]), 7)
        self.assertEqual(kadanes_v2([1, 2, -3, 2, 5]), 7)

    def test_missing(self):
        self.assertEqual(missing([1, 2, 3, 5]), [4])
        self.assertEqual(missing([-1, 2, 3, 4, 5]), [0, 1])
        self.assertEqual(missing([1, 5]), [2, 3, 4])
        self.assertEqual(missing([-3, 2]), [-2, -1, 0, 1])

    def test_substring_sum(self):
        self.assertEqual(substring_sum('16'), 23)

    def test_max_subarray(self):
        self.assertEqual(max_subarray([1, 2, 3, 4]), (10, 10))
        self.assertEqual(max_subarray([2, -1, 2, 3, 4, -5]), (10, 11))
        self.assertEqual(max_subarray([-100, -1]), (-1, -1))
        self.assertEqual(max_subarray([1]), (1, 1))

