import unittest


class Graphs.Tree:
    def __init__(self):
        self.root = None
        self.leaves = []

    def add_root(self, value):
        root = self.Leaf(value)
        self.root = root
        self.leaves.append(root)

    def add_node(self, leaf_node, left=None, right=None):
        left_leaf = None if left is None else self.Leaf(left)
        right_leaf = None if right is None else self.Leaf(right)

        for leaf in self.leaves:
            if leaf.value == leaf_node:
                leaf.set_left(left_leaf)
                leaf.set_right(right_leaf)
                self.leaves.extend([left_leaf, right_leaf])
                return

        raise Exception('Graphs.Node {0} not found'.format(leaf_node))

    def get_leaf(self, value):
        for leaf in self.leaves:
            if leaf.value == value:
                return value

    def append_to_leaf(self, leaf_value, left=None, right=None):
        for leaf in self.leaves:
            if leaf.value == leaf_value:
                # Make new leaves
                left_leaf = self.Leaf(left)
                right_leaf = self.Leaf(right)
                # Set leaves
                leaf.set_left(left_leaf)
                leaf.set_right(right_leaf)

    def _bst(self, node):
        is_bst = True

        if node is None:
            return is_bst

        if node.left and node.left.value < node.value:
            is_bst = is_bst and self._bst(node.left)
        else:
            is_bst = is_bst and False
        if node.right and node.right.value > node.value:
            is_bst = is_bst and self._bst(node.right)
        else:
            is_bst = is_bst and False

        return is_bst

    def bst(self):
        return self._bst(self.root)

    class Leaf:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        def set_left(self, left):
            self.left = left

        def set_right(self, right):
            self.right = right

    # Tie the algoritms in here
    def left_tree(self):
        """
            Given an array return the left most branches of the tree
        :return:
        """
        left_array = []

        next_leaf = self.root
        while next_leaf:
            left_array.append(next_leaf.value)
            next_leaf = next_leaf.left if next_leaf.left is not None else next_leaf.right

        return left_array

    def vertical_line(self, vertical_line_array, leaf, line_number, horizontal_distance):
        """
            Get tree as a vertical line
        :param leaf:
        :param line_number: Current vertical line
        :param horizontal_distance:
        :return:
        """
        if leaf is None:
            return

        if horizontal_distance == line_number:
            vertical_line_array.append(leaf.value)

        self.vertical_line(vertical_line_array, leaf.left, line_number, horizontal_distance - 1)
        self.vertical_line(vertical_line_array, leaf.right, line_number, horizontal_distance + 1)

        return vertical_line_array

    def find_min_max(self, leaf, min, max, horizontal_distance):
        """
            Find the min and max of a tree recursively. Min and max are arrays
            because that will make them mutable in python
        :param root: Leaf object
        :param min: array representing min distance to root
        :param max: array representing max distance to root
        :param horizontal_distance:
        :return:
        """
        if leaf is None:
            return None

        if min[0] > horizontal_distance:
            min[0] = horizontal_distance
        elif max[0] < horizontal_distance:
            max[0] = horizontal_distance

        self.find_min_max(leaf.left, min, max, horizontal_distance - 1)
        self.find_min_max(leaf.right, min, max, horizontal_distance + 1)

    def vertical_order(self):
        """
            Vertical print of the tree, meaning the left most nodes, then root then
            right most.Min and max are arrays because that will make them mutable in python
        :return:
        """
        min = [0]
        max = [0]
        # Get the min an max line numbers
        self.find_min_max(self.root, min, max, 0)
        # Get tree as vertical array using those line numbers
        vertical_array = []
        # Min and max values
        min_val = min[0]
        max_val = max[0]
        for line_number in range(min_val, max_val + 1):
            self.vertical_line(vertical_array, self.root, line_number, 0)

        return vertical_array


class Test(unittest.TestCase):

    def setUp(self):
        self.t = Graphs.Tree()
        self.t.add_root(10)
        self.t.add_node(10, left=2, right=3)
        self.t.add_node(2, left=4, right=5)
        self.t.add_node(3, left=6, right=7)
        self.t.add_node(4, right=8)

        self.t1 = Graphs.Tree()
        self.t1.add_root(1)
        self.t1.add_node(1, left=2, right=3)
        self.t1.add_node(2, left=4, right=5)
        self.t1.add_node(3, left=6, right=7)
        self.t1.add_node(6, right=8)
        self.t1.add_node(7, right=9)

    def test_left_tree(self):
        self.assertEqual(self.t.left_tree(), [10, 2, 4, 8])

    def test_vertical_order(self):
        self.assertEqual(self.t1.vertical_order(), [4, 2, 1, 5, 6, 3, 8, 7, 9])

    def test_bst(self):
        self.assertFalse(self.t.bst())
        self.assertFalse(self.t1.bst())

        t = Graphs.Tree()
        t.add_root(2)
        t.add_node(2, left=1, right=4)
        t.add_node(4, left=3, right=5)
        self.assertTrue(t.bst())
