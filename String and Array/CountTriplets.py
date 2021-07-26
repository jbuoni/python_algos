"""
    Count the triplets in array. A triplet is where the sum of the three items
    is less than the inputted sum
"""
import unittest
import math


def merge(array):
    if len(array) > 1:

        mid = int(math.ceil(len(array) / 2))

        left = array[:mid]
        right = array[mid:]

        merge(left)
        merge(right)


def count_triplets(array, sum):
    """
        O(n^2)
    :param array:
    :param sum:
    :return:
    """
    length = len(array)

    if length == 0 or (length == 1 and sum != array[0]):
        return 0

    # Sort the array first, then check for triplets
    merge(array)

    num_trips = 0

    # Now loop through the array twice. We know if we
    # are past the sum we know it is not a triplet
    for i in range(0, length - 2):
        j = i + 1
        k = length - 1

        # Go from start and end. Meet in middle
        while j < k:
            temp_sum = array[i] + array[j] + array[k]

            # If we are past the sum, then drop k
            # This works because the array is sorted
            if temp_sum >= sum:
                k = k - 1
            else:
                num_trips += (k - j)
                j += 1

    return num_trips


class Test(unittest.TestCase):
    def test_count_triplets(self):
        self.assertEqual(count_triplets([5, 1, 3, 4, 7], 12), 4)
        self.assertEqual(count_triplets([-2, 0, 1, 3], 2), 2)
        self.assertEqual(count_triplets([-2, 0, 1, 3], -9), 0)
