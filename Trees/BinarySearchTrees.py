import unittest


class BinaryTree:
    def __init__(self, root):
        self.root = self.Graphs.Node(root)

    class Graphs.Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        def set_left(self, left):
            self.left = left

        def set_right(self, right):
            self.right = right

    def insert(self, node_value, node=None):
        """
            Recursive function used to insert node
        :param node_value:
        :param node:
        :return:
        """
        # Determine what node is
        if self.root is None:
            self.root = self.Graphs.Node(node_value)
        elif node is None:
            node = self.root
        # Now do insert
        if node.value > node_value:
            if node.left is None:
                node.left = self.Graphs.Node(node_value)
            else:
                self.insert(node_value, node=node.left)
        else:
            if node.right is None:
                node.right = self.Graphs.Node(node_value)
            else:
                self.insert(node_value, node=node.right)

    def search(self, value):
        """
            If value is greater, then search left
            else search right
        :param value:
        :return: Graphs.Node
        """
        node = self.root

        while node:
            if node.value == value:
                return node
            if node.value > value:
                # search left
                node = node.left
            elif node.value < value:
                # search right
                node = node.right

    def _get_sorted(self, node, sorted):
        if node is None:
            return
        self._get_sorted(node.left, sorted)
        sorted.append(node.value)
        self._get_sorted(node.right, sorted)

    def as_arr_sorted(self):
        sorted = []

        if self.root:
            self._get_sorted(self.root, sorted)

        return sorted

    def _get_bottom(self, node, bottom):
        if node.left is None and node.right is None:
            bottom.append(node.value)
        else:
            if node.left:
                self._get_bottom(node.left, bottom)
            if node.right:
                self._get_bottom(node.right, bottom)

    def get_bottom(self):
        bottom = []
        self._get_bottom(self.root, bottom)
        return bottom


class Test(unittest.TestCase):

    def test_search(self):
        t = BinaryTree(2)
        t.insert(1)
        t.insert(3)
        t.insert(5)

        self.assertEqual(t.search(3).right.value, 5)

    def test_as_arr_sorted(self):
        t = BinaryTree(2)
        t.insert(1)
        t.insert(3)
        t.insert(5)

        self.assertEqual(t.as_arr_sorted(), [1, 2, 3, 5])

    def test_get_bottom(self):
        t = BinaryTree(2)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(6)
        t.insert(7)

        self.assertEqual(t.get_bottom(), [1, 7])

