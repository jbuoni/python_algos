import unittest


class Queue:
    """
        We don't really need this, but it makes
        clear that we are using a stack. _stack
        is denoted as private so we can make it
        clear that the object should not be used
    """
    def __init__(self, items):
        self._queue = [item for item in items] if items else []

    def push(self, item):
        self._queue.append(item)

    def pop(self):
        return self._queue.pop(0)

    def is_empty(self):
        return len(self._queue) == 0


def next_largest(array):
    """
        Given a sorted array, get the next largest element in that array.
        Time complexity O(2n)
    :param array:
    :return:
    """
    queue = Queue(array)
    return_arr = [-1 for j in range(len(array))]

    for i in range(len(array)):
        while not queue.is_empty():
            queue_item = queue.pop()
            if array[i] < queue_item:
                return_arr[i] = queue_item
                break

    return return_arr


class Test(unittest.TestCase):
    def test_matching(self):
        self.assertEqual(next_largest([1, 2, 3, 4]), [2, 3, 4, -1])
        self.assertEqual(next_largest([1, 3, 4, 2]), [3, 4, -1, -1])
        self.assertEqual(next_largest([1, 3, 4, 2, 5]), [3, 4, 5, -1, -1])
