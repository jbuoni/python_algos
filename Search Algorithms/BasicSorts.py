
import math
import unittest


def merge(array):
    """
        Merge sort algorithm. Split up into smaller chunks, then
        sort the small in a bottom up fashion
        O(n log n)
        Space complexity O(n)
    :param array:
    :return:
    """

    if len(array) > 1:
        mid = int(math.ceil(len(array) / 2))

        left = array[:mid]
        right = array[mid:]

        merge(left)
        merge(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # If there was anything left over (i + j < k) then copy it
        # This will be the case while we are in the stages where
        # the array is still chunked
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


def bubble(array):
    """
        Time Complexity O(n^2)
        Space Complexity O(n)
    :param array:
    :return:
    """

    for i in range(len(array)):
        start = len(array) - i - 1
        for j in range(start, len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def insertion(array):
    """
        Time Complexity O(n^2)
        Space Complexity O(n)
    :param array:
    :return:
    """
    for i in range(1, len(array)):
        j = i - 1
        node = array[i]

        # Move through each element
        while j >= 0 and array[j] > node:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = node

    return array


def make_heap(array, length, i):
    """
    Convert array into a heap
    :param array:
    :param length:
    :param i:
    :return:
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # See if the left child of the root exists and is
    # larger than the root
    if left < length and array[largest] < array[left]:
        largest = left

    if right < length and array[largest] < array[right]:
        largest = right

    # The largest node is now the root
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        make_heap(array, length, largest)


def heap(array):
    """
        Time complexity to build the heap is O(n) and the
        time complexity to sort is O(log n) so the total complexity
        is O(n log n)

        space complexity is O(n)
    :param array:
    :return:
    """
    length = len(array)

    # Build the heap
    for i in range(length, -1, -1):
        make_heap(array, length, i)

    # Get items off the heap
    for j in range(length - 1, 0, -1):
        array[0], array[j] = array[j], array[0]
        make_heap(array, j, 0)

    return array


def partition(array, low, high):
    index = low - 1
    pivot = array[high]

    for j in range(low, high):
        # If the current value is less than the pivot swap
        if array[j] < pivot:
            index += 1
            array[j], array[index] = array[index], array[j]

    array[high], array[index + 1] = array[index + 1], array[high]

    return index + 1


def quick(array, low, high):
    """
        Time complexity to build the heap is O(n) and the
        time complexity to sort is O(log n) so the total complexity
        is O(log n)

        space complexity is O(n)
    :param array:
    :param low:
    :param high:
    :return:
    """

    if len(array) <= 1:
        return array

    if low < high:
        pivot = partition(array, low, high)
        # Sort on the pivot
        quick(array, low, pivot - 1)
        quick(array, pivot + 1, high)

        return array  # For testing


class Test(unittest.TestCase):
    def test_merge(self):
        test_array = merge([2, 3, 4, 1])
        self.assertEqual(test_array, [1, 2, 3, 4])
        test_array = merge([9, 99, 999, 99, 9])
        self.assertEqual(test_array, [9, 9, 99, 99, 999])
        test_array = merge([5, 4, 3, 2, 1])
        self.assertEqual(test_array, [1, 2, 3, 4, 5])
        test_array = merge([103])
        self.assertEqual(test_array, [103])
        test_array = merge([])
        self.assertEqual(test_array, [])
        test_array = merge([5, 55])
        self.assertEqual(test_array, [5, 55])
        test_array = merge([1, 2, 3, 4, 5])
        self.assertEqual(test_array, [1, 2, 3, 4, 5])

    def test_bubble(self):
        test_array = bubble([2, 3, 4, 1])
        self.assertEqual(test_array, [1, 2, 3, 4])
        test_array = bubble([9, 99, 999, 99, 9])
        self.assertEqual(test_array, [9, 9, 99, 99, 999])
        test_array = bubble([5, 4, 3, 2, 1])
        self.assertEqual(test_array, [1, 2, 3, 4, 5])
        test_array = bubble([103])
        self.assertEqual(test_array, [103])
        test_array = bubble([])
        self.assertEqual(test_array, [])
        test_array = bubble([5, 55])
        self.assertEqual(test_array, [5, 55])
        test_array = bubble([1, 2, 3, 4, 5])
        self.assertEqual(test_array, [1, 2, 3, 4, 5])

    def test_insertion(self):
        test_array = insertion([2, 3, 4, 1])
        self.assertEqual(test_array, [1, 2, 3, 4])
        test_array = insertion([9, 99, 999, 99, 9])
        self.assertEqual(test_array, [9, 9, 99, 99, 999])
        test_array = insertion([5, 4, 3, 2, 1])
        self.assertEqual(test_array, [1, 2, 3, 4, 5])
        test_array = insertion([103])
        self.assertEqual(test_array, [103])
        test_array = insertion([])
        self.assertEqual(test_array, [])
        test_array = insertion([5, 55])
        self.assertEqual(test_array, [5, 55])
        test_array = insertion([1, 2, 3, 4, 5])
        self.assertEqual(test_array, [1, 2, 3, 4, 5])

    def test_heap(self):
        test_array = heap([2, 3, 4, 1])
        self.assertEqual(test_array, [1, 2, 3, 4])
        test_array = heap([9, 99, 999, 99, 9])
        self.assertEqual(test_array, [9, 9, 99, 99, 999])
        test_array = heap([5, 4, 3, 2, 1])
        self.assertEqual(test_array, [1, 2, 3, 4, 5])
        test_array = heap([103])
        self.assertEqual(test_array, [103])
        test_array = heap([])
        self.assertEqual(test_array, [])
        test_array = heap([5, 55])
        self.assertEqual(test_array, [5, 55])
        test_array = heap([1, 2, 3, 4, 5])
        self.assertEqual(test_array, [1, 2, 3, 4, 5])

    def test_quick(self):
        test_array = quick([2, 3, 4, 1], 0, 3)
        self.assertEqual(test_array, [1, 2, 3, 4])
        test_array = quick([9, 99, 999, 9], 0, 3)
        self.assertEqual(test_array, [9, 9, 99, 999])
        test_array = quick([5, 4, 3, 2, 1], 0, 4)
        self.assertEqual(test_array, [1, 2, 3, 4, 5])
        test_array = quick([103], 0, 0)
        self.assertEqual(test_array, [103])
        test_array = quick([], 0, 0)
        self.assertEqual(test_array, [])
        test_array = quick([5, 55], 0, 1)
        self.assertEqual(test_array, [5, 55])
        test_array = quick([1, 2, 3, 4, 5], 0, 4)
        self.assertEqual(test_array, [1, 2, 3, 4, 5])
