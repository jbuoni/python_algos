import unittest
import constants


class Stack:
    """
        We don't really need this, but it makes
        clear that we are using a stack. _stack
        is denoted as private so we can make it
        clear that the object should not be used
    """
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def is_empty(self):
        return len(self._stack) == 0


class StackMin:
    """
        Special class used to get the min item on the
        stack. Comprised of multiple
    """

    def __init__(self):
        self.top = None
        self.minimum = None

    def push(self, value):
        # Make node value initially
        node = self.Graphs.Node(value)

        if self.top is None or value < self.minimum:
            node = self.Graphs.Node(value) if self.top is None else self.Graphs.Node((2 * value) - self.minimum)
            self.minimum = value

        node.next = self.top if self.top is not None else None
        self.top = node  # It has always been assigned by this point

    def pop(self):
        """
            We don't actually return the top,
            but min value or (2 * min) - value
        :return:
        """
        if self.top is None:
            return None

        node = self.top
        self.top = node.next

        if node.value < self.minimum:
            self.minimum = (2 * self.minimum) - node.value

        return node.value

    def get_min(self):
        return self.minimum

    class Graphs.Node:
        def __init__(self, value):
            self.value = value
            self.next = None


def matching(str_arr):
    """
        Given a string array, determine if the string
        contains a valid sequence of open and closed
        parenthesis. EX: '[()]{}{[()()]()}'
        Time complexity O(n)
        Space complexity O(n + m/2)
    :param str_arr:
    :return:
    """
    stack = Stack()

    def get_end_char(start_character):
        if start_character == constants.BRACKET:
            return constants.BRACKET_END
        elif start_character == constants.PARENTHISIS:
            return constants.PARENTHISIS_END
        elif start_character == constants.SQUARE_BRACKET:
            return constants.SQUARE_BRACKET_END
        else:
            # Should never happen
            return ''

    for current_chr in str_arr:
        if constants.is_start(current_chr):
            char_to_push = get_end_char(current_chr)
            stack.push(char_to_push)
        elif constants.is_end(current_chr):
            comp_char = stack.pop()
            if comp_char != current_chr:
                return False

    # When we are done, see if the stack is empty. If so, return true
    return stack.is_empty()


class Test(unittest.TestCase):
    def test_matching(self):
        self.assertTrue(matching(['{', '[', '(', ')', ']', '}']))
        self.assertTrue(matching(['{', '[', '(', ')', ']', '}', '[', ']']))
        self.assertTrue(matching(['{', '[', '(', '{', '}', ')', ']', '}']))
        self.assertFalse(matching(['{', '[', '(', ')', ']']))
        self.assertFalse(matching(['{', '[', ')', ']', '}']))

    def test_StackMin(self):
        stack = StackMin()

        stack.push(3)
        stack.push(5)
        self.assertEqual(stack.get_min(), 3)
        stack.push(2)
        stack.push(1)
        self.assertEqual(stack.get_min(), 1)
        stack.pop()
        self.assertEqual(stack.get_min(), 2)

