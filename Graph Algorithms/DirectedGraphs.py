"""
    Depth first search algorithm. Uses a graph with nodes and edges
    Ensures we do not mark cycles twice.

    Time complexity: O(V^2), can be reduced to O(E log V) with binary heap
    Space complexity is O(2V)
"""

from collections import defaultdict
import unittest


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    # Directional edges
    def add_egde(self, node_f, node_t):
        self.graph[node_f].append(node_t)

        # Check to see if there is a new vertex
        if not self.graph[node_t]:
            self.graph[node_t] = []

    def depth_first_search(self):
        visited = {}
        path = []
        for node in self.graph:
            if node not in visited:
                path.append(node)
                visited[node] = True
            # For each node, visit edges if no visited
            for edge in self.graph[node]:
                if edge not in visited:
                    path.append(edge)
                    visited[edge] = True

        return path, visited

    def breath_first_search(self, start):
        visited = {}
        queue = []
        path = []

        # Add start node. From here, get all nodes
        queue.append(start)
        path.append(start)
        visited[start] = True

        while queue:
            node_idx = queue.pop(0)

            for node in self.graph[node_idx]:
                if node not in visited.keys():
                    queue.append(node)
                    path.append(node)
                    visited[node] = True

        # Get nodes missed

        return path, visited

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

    def _detect_cycle(self, node_idx, visited, recursive_stack):
        visited[node_idx] = True
        recursive_stack[node_idx] = True

        # Do a DFS (ish), and if there is a node that is visited twice
        # from the same parent node then there is a cycle
        for neighbour in self.graph[node_idx]:
            if not visited[neighbour]:
                if self._detect_cycle(neighbour, visited, recursive_stack):
                    return True
            elif recursive_stack[neighbour]:
                return True

        # Set this back to false
        recursive_stack[node_idx] = False
        return False

    def detect_cycle(self):
        """
            Return true if there is a cycle in the
            graph and false otherwise
            complexity of O(E log V)
        :return:
        """
        visited = [False] * len(self.graph)
        recursive_stack = [False] * len(self.graph)

        for i in self.graph:
            if not visited[i]:
                if self._detect_cycle(i, visited, recursive_stack):
                    return True
        return False


class Test(unittest.TestCase):
    def setUp(self):
        g = Graph()
        g.add_egde(0, 1)
        g.add_egde(0, 2)
        g.add_egde(1, 2)
        g.add_egde(2, 0)
        g.add_egde(2, 3)
        g.add_egde(3, 3)

        self.graph = g

    def test_depth_first_search(self):
        path, visited = self.graph.depth_first_search()
        self.assertEqual([0, 1, 2, 3], path)
        self.assertEqual([0, 1, 2, 3], list(visited.keys()))

        # Edge that goes nowhere
        self.graph.add_egde(4, 4)

        path, visited = self.graph.depth_first_search()
        self.assertEqual([0, 1, 2, 3, 4], path)
        self.assertEqual([0, 1, 2, 3, 4], list(visited.keys()))

    def test_breath_first_search(self):
        path, visited = self.graph.breath_first_search(2)
        self.assertEqual([2, 0, 3, 1], path)
        self.assertEqual([True, True, True, True], visited.values())

    def test_detect_cycle(self):
        g = Graph()
        g.add_egde(0, 1)
        g.add_egde(0, 2)
        g.add_egde(0, 3)

        self.assertTrue(self.graph.detect_cycle())
        self.assertFalse(g.detect_cycle())

    def test_build_matrix(self):
        matrix = [
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 1],
            [0, 0, 0, 1]
        ]

        graph_matrix = self.graph.build_matrix()
        self.assertEqual(graph_matrix, matrix)
