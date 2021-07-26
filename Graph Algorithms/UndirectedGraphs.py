import unittest
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, node_t, node_f):
        self.graph[node_t].append(node_f)
        self.graph[node_f].append(node_t)

    def _detect_cycle(self, node_idx, parent_node, visited):
        visited[node_idx] = True
        # Do a DFS (ish), and if there is a node that is visited twice
        # from the same parent node then there is a cycle
        for i in self.graph[node_idx]:
            if not visited[i]:
                if self._detect_cycle(i, node_idx, visited):
                    return True
            elif i != parent_node:
                return True
        return False

    def detect_cycle(self):
        """
            Return true if there is a cycle in the
            graph and false otherwise
            complexity of O(E log V)
        :return:
        """
        visited = [False] * len(self.graph)

        for i in self.graph:
            if not visited[i]:
                # Default parent to -1
                if self._detect_cycle(i, -1, visited):
                    return True
        return False

    def build_matrix(self):
        """
            Return a matrix representation of the graph
            O(VE)
        :return:
        """
        matrix = [[0 for x in range(len(self.graph))] for y in range(len(self.graph))]

        for node in self.graph:
            for edge in self.graph[node]:
                matrix[node][edge] = 1

        return matrix

    def dfs_matrix(self, matrix, row, col):
        """
            Special DFS search for matrix graph representation
        :param matrix:
        :param row:
        :param col:
        :return:
        """
        row_len = len(matrix)
        col_len = len(matrix[0])

        if matrix[row][col] == 0:
            return

        matrix[row][col] = 0

        if row != 0:
            self.dfs_matrix(matrix, row - 1, col)
        if row != row_len - 1:
            self.dfs_matrix(matrix, row + 1, col)
        if col != 0:
            self.dfs_matrix(matrix, row, col - 1)
        if col != col_len - 1:
            self.dfs_matrix(matrix, row, col + 1)

    def count_islands(self, matrix=None):
        """
            Return the number of islands in a graph.
            An island is where all nodes are not connected
            to an outer node
            O(VE)
        :param matrix:
        :return:
        """
        matrix = self.build_matrix() if matrix is None else matrix

        island_count = 0

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    self.dfs_matrix(matrix, i, j)
                    island_count += 1

        return island_count


class Test(unittest.TestCase):
    def setUp(self):
        g = Graph()
        g.add_edge(1, 0)
        g.add_edge(0, 2)
        g.add_edge(2, 0)
        g.add_edge(0, 3)
        g.add_edge(3, 4)
        self.graph = g

    def test_detect_cycle(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)

        self.assertTrue(self.graph.detect_cycle())
        self.assertFalse(g.detect_cycle())

    def test_build_matrix(self):
        matrix = [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0]
        ]

        graph_matrix = self.graph.build_matrix()
        self.assertEqual(graph_matrix, matrix)

    def test_count_islands(self):
        matrix = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]
        ]

        island_count = self.graph.count_islands(matrix=matrix)
        self.assertEqual(island_count, 6)
