import unittest


def merge_sorted_arrays(array1, array2):
    """
        Merge two arrays that are already sorted
        should remain sorted. Allows for extra space

        O(nm)
    :param array1:
    :param array2:
    :return:
    """

    len_a1 = len(array1)
    len_a2 = len(array2)
    i = j = 0
    sorted_array = []

    while i < len_a1 and j < len_a2:
        if array1[i] > array2[j]:
            sorted_array.append(array2[j])
            j += 1
        else:
            sorted_array.append(array1[i])
            i += 1

    # Everything left should just be appended.
    append_1 = array1[i:] if i < len_a1 else []
    append_2 = array2[j:] if j < len_a2 else []

    sorted_array = sorted_array + append_1 + append_2

    return sorted_array


def merge_sorted_arrays_no_extra_array(array1, array2):
    """
        Merge two arrays that are already sorted
        should remain sorted. Does not allow for extra space

        O(nm)
    :param array1:
    :param array2:
    :return:
    """
    idx = 0

    while len(array2) and idx < len(array1):
        if array1[idx] > array2[0]:
            array1.insert(idx, array2[0])
            array2.pop(0)
        else:
            idx += 1

    array1 += array2
    return array1


def rearrange_array_alternate(array):
    """
        Rearrange to sorted arrays where its [max, min, max2, min2]
        with a space complexity of O(1)
    :param array1:
    :param array2:
    :return:
    """

    for j in range(0, len(array) - 1, 2):
        array.insert(j, array[len(array) - 1])
        array.pop(len(array) - 1)

    return array


class Test(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        a1 = [1, 3, 4]
        a2 = [2, 5]
        self.assertEqual(merge_sorted_arrays(a1, a2), [1, 2, 3, 4, 5])
        a1 = [1, 3, 4, 5]
        a2 = [-2, 5]
        self.assertEqual(merge_sorted_arrays(a1, a2), [-2, 1, 3, 4, 5, 5])
        a1 = [1, 2, 3, 4, 5, 6]
        a2 = [7, 8, 9]
        self.assertEqual(merge_sorted_arrays(a1, a2), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        a1 = [1, 4, 6]
        a2 = [2, 7]
        self.assertEqual(merge_sorted_arrays(a1, a2), [1, 2, 4, 6, 7])

    def test_merge_sorted_arrays_same_memory(self):
        a1 = [1, 3, 4]
        a2 = [2, 5]
        self.assertEqual(merge_sorted_arrays_no_extra_array(a1, a2), [1, 2, 3, 4, 5])
        a1 = [1, 3, 4, 5]
        a2 = [-2, 5]
        self.assertEqual(merge_sorted_arrays_no_extra_array(a1, a2), [-2, 1, 3, 4, 5, 5])
        a1 = [1, 2, 3, 4, 5, 6]
        a2 = [7, 8, 9]
        self.assertEqual(merge_sorted_arrays_no_extra_array(a1, a2), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        a1 = [1, 4, 6]
        a2 = [2, 7]
        self.assertEqual(merge_sorted_arrays_no_extra_array(a1, a2), [1, 2, 4, 6, 7])

    def test_rearrange_array_alternate(self):
        self.assertEqual(rearrange_array_alternate([1, 3, 4]), [4, 1, 3])
        self.assertEqual(rearrange_array_alternate([1, 3, 4, 5]), [5, 1, 4, 3])
        self.assertEqual(rearrange_array_alternate([1, 2, 3, 4, 5, 6]), [6, 1, 5, 2, 4, 3])
        self.assertEqual(rearrange_array_alternate([1]), [1])
        self.assertEqual(rearrange_array_alternate([]), [])
