"""
    Given a matrix of size NxM where every element is either 'O' or 'X',
    replace 'O' with 'X' if surrounded by 'X'. A 'O' (or a set of 'O') is
    considered to be by surrounded by 'X' if there are 'X' at locations just
    below, just above, just left and just right of it.

    https://practice.geeksforgeeks.org/problems/replace-os-with-xs/0
    https://en.wikipedia.org/wiki/Flood_fill
    
    Time complexity O(NM)
    Space complexity O(NM)
"""
import unittest
from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.num_rows = 0
        self.num_cols = 0

    def set_graph(self, graph):
        self.graph = graph
        self.num_rows = len(self.graph)
        self.num_cols = len(self.graph[0])

    def flood_fill(self, x, y, old_val, new_val):
        """
            Recursive algorithm.
            Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K), your task is to
            replace color of the given pixel and all adjacent(excluding diagonally adjacent) same colored
            pixels with the given color K.

            Check to see if color is new or old value. If not, then return, else change and check the cells
            around it for 1 +/- x and y
        :param x:
        :param y:
        :param old_val:
        :param new_val:
        :return:
        """

        # Doing it this way so I can clearly see edge cases
        if x < 0 or y < 0 or x >= self.num_rows or y >= self.num_cols:
            # Out of bounds
            return
        elif self.graph[x][y] == new_val:
            # Already new color
            return
        elif self.graph[x][y] != old_val:
            # Not a cell to replace
            return

        self.graph[x][y] = new_val

        # For all cells next to this, do the same thing
        self.flood_fill(x + 1, y, old_val, new_val)
        self.flood_fill(x, y + 1, old_val, new_val)
        self.flood_fill(x - 1, y, old_val, new_val)
        self.flood_fill(x, y - 1, old_val, new_val)

    def replace_xs_os(self):
        """
            Use the flood fill algorithm
        :param graph:
        :return:
        """
        # First replace all 'O's with '*'
        for x in range(self.num_rows):
            for y in range(self.num_cols):
                if self.graph[x][y] == 'O':
                    self.graph[x][y] = '*'

        # Now run the flood fill algorithm on edges
        for x in range(self.num_rows):
            # Top
            self.flood_fill(x, 0, '*', 'O')

        for x in range(self.num_rows):
            # Top
            self.flood_fill(x, self.num_cols - 1, '*', 'O')

        for y in range(self.num_cols):
            # Left
            self.flood_fill(0, y, '*', 'O')

        for y in range(self.num_cols):
            # Left
            self.flood_fill(self.num_rows - 1, y, '*', 'O')

        # Now replace all remaining '*' with 'O'
        for x in range(self.num_rows):
            for y in range(self.num_cols):
                if self.graph[x][y] == '*':
                    self.graph[x][y] = 'X'

        return self.graph


class Test(unittest.TestCase):

    def test_replace_xs_os(self):
        graph = [['X', 'O', 'X', 'X', 'X', 'X'],
                 ['X', 'O', 'X', 'X', 'O', 'X'],
                 ['X', 'X', 'X', 'O', 'O', 'X'],
                 ['O', 'X', 'X', 'X', 'X', 'X'],
                 ['X', 'X', 'X', 'O', 'X', 'O'],
                 ['O', 'O', 'X', 'O', 'O', 'O']]

        graph_obj = Graph()

        graph_obj.set_graph(graph)

        result = graph_obj.replace_xs_os()

        expected = [['X', 'O', 'X', 'X', 'X', 'X'],
                    ['X', 'O', 'X', 'X', 'X', 'X'],
                    ['X', 'X', 'X', 'X', 'X', 'X'],
                    ['O', 'X', 'X', 'X', 'X', 'X'],
                    ['X', 'X', 'X', 'O', 'X', 'O'],
                    ['O', 'O', 'X', 'O', 'O', 'O']]

        self.assertEqual(result, expected)
