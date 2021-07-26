"""
    Given a list of numbers (in some cases sorted, others no), and an integer value, 
    determine if the sum of the integer value is contained within the list of items 
"""

import unittest


# Get min and max locations, then from here, determine if the sum exists
# Sum up those values, if its too high move the max down, and too low
# the min down. From there we know if there is the sum because the list
# is sorted
def sum_exists_sorted(arr, sum_val):
    min_idx = 0
    max_idx = len(arr) - 1

    # Not equal to because you cant use the same value twice
    while max_idx > min_idx:
        sum = int(arr[min_idx] + arr[max_idx])
        if sum == sum_val:
            return arr[min_idx], arr[max_idx]
        elif sum < sum_val:
            min_idx += 1
        elif sum > sum_val:
            max_idx -= 1
    return -1, -1


# Same as above but with a bit of recursion
def sum_exists_sorted_recursive(arr, sum_val):

    def sum_exists(min_idx, max_idx):
        sum = arr[min_idx] + arr[max_idx]
        if max_idx <= min_idx:
            return -1, -1
        elif sum < sum_val:
            min_idx += 1
            return sum_exists(min_idx, max_idx)
        elif sum > sum_val:
            max_idx -= 1
            return sum_exists(min_idx, max_idx)
        elif sum == sum_val:
            return arr[min_idx], arr[max_idx]

    return sum_exists(0, len(arr) - 1)


# If the array is not sorted, we can't actually tell if there is a larger
# or smaller number in the array easily. Sorting is fine here, but instead
# lets do a bit better and use a hash table. For each item in the array
# Store what would be needed to make the sum as a hash, if that exists
# later then we have the sum
def sum_exists_non_sorted(arr, sum_val):
    sum_hash = {}
    # Loop through
    for item in arr:
        difference = sum_val - item
        # If there is a match, then we have it
        if difference in sum_hash:
            return difference, item

        sum_hash[item] = True

    return -1, -1



def subset_sum_bool(array, sum):
    """
    :param array:
    :param sum:
    :return: True if there is a subset and false otherwise
    """

    length = len(array)

    # Just break out here
    if length == 0 or (length == 1 and sum != array[0]):
        return False

    t = [[False for i in range(sum + 1)] for j in range(length + 1)]

    for i in range(length + 1):
        t[i][0] = True

    # Build in a bottom up manner
    for i in range(length + 1):
        for j in range(sum + 1):
            t[i][j] = t[i - 1][j]
            # If the previous value has a sum and we can fit this, return true
            if array[i - 1] <= j:
                t[i][j] = t[i][j] or t[i - 1][j - array[i - 1]]

    return t[length][sum]


def subset_sum(array, sum):
    """
        Time and Space complexity O(n)
    :param array:
    :param sum:
    :return: The start and end index of the sum and -1 otherwise
    """

    length = len(array)

    # Just break out here
    if length == 0 or (length == 1 and sum != array[0]):
        return -1

    current_sum = array[0]
    start = 0
    index = 1

    # Iterate through the array and see if we are at the sum yet
    # If we are over current sum, then subtract start from the
    # sum value, removing it from the array
    while index < length:
        while current_sum > sum and start < index - 1:
            current_sum = current_sum - array[start]
            start += 1
        # We have found the sub array
        if current_sum == sum:
            return start, index - 1

        if index < length:
            current_sum += array[index]

        index += 1

    return -1


class TestArraySum(unittest.TestCase):

    array_with_sum_sorted = [1, 2, 3, 4, 5, 9]
    array_with_sum_not_sorted = [1, 4, 3, 5, 6]
    array_with_no_sum_sorted = [1, 2, 3, 4, 9]
    array_with_no_sum_not_sorted = [1, 9, 4, 5, 2]
    sum = 8

    def test_sum_exists_sorted(self):
        result = sum_exists_sorted(self.array_with_sum_sorted, self.sum)
        self.assertEqual(result, (3, 5))
        result = sum_exists_sorted(self.array_with_no_sum_sorted, self.sum)
        self.assertEqual(result, (-1, -1))
        pass

    def test_sum_exists_sorted_recursive(self):
        result = sum_exists_sorted_recursive(self.array_with_sum_sorted, self.sum)
        self.assertEqual(result, (3, 5))
        result = sum_exists_sorted_recursive(self.array_with_no_sum_sorted, self.sum)
        self.assertEqual(result, (-1, -1))
        pass

    def test_sum_exists_non_sorted(self):
        result = sum_exists_non_sorted(self.array_with_sum_sorted, self.sum)
        self.assertEqual(result, (3, 5))
        result = sum_exists_non_sorted(self.array_with_no_sum_sorted, self.sum)
        self.assertEqual(result, (-1, -1))
        result = sum_exists_non_sorted(self.array_with_sum_not_sorted, self.sum)
        self.assertEqual(result, (3, 5))
        result = sum_exists_non_sorted(self.array_with_no_sum_not_sorted, self.sum)
        self.assertEqual(result, (-1, -1))
        pass

    def test_subset_sum_bool(self):
        self.assertTrue(subset_sum_bool([3, 34, 4, 12, 5, 2], 9))
        self.assertTrue(subset_sum_bool([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
        self.assertTrue(subset_sum_bool([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
        self.assertFalse(subset_sum_bool([3, 34, 4, 12, 5, 2], 999))

    def test_subset_sum(self):
        self.assertEqual(subset_sum([15, 2, 4, 8, 9, 5, 10, 23], 23), (1, 4))
        self.assertEqual(subset_sum([3, 34, 4, 12, 5, 2], 999), - 1)
        self.assertEqual(subset_sum([3, 34, 4, 12, 5, 2], 9), -1)
        self.assertEqual(subset_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9), (1, 3))
        self.assertEqual(subset_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), (4, 5))


if __name__ == '__main__':
    unittest.main()
