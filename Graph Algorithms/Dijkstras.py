"""
    Dijkstras shortest path alrgorith finds the shortest path from one node to all
    other nodes in the graph. It checks each neighboring nodes, and determines the shortest path
    to that node. Then from each node, it determines the shortest path to all unvisited nodes
"""
import unittest
import sys


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def min_distance(self, dist, visited):

        # Initilaize minimum distance for next node
        min_distance = sys.maxint
        min_index = None  # Shouldn't ever matter

        # Search not nearest vertex not in the
        # shortest path tree
        for vertex in range(self.V):
            if dist[vertex] < min_distance and visited[vertex] is False:
                min_distance = dist[vertex]
                min_index = vertex

        return min_index


    def dijkstras(self, start_node):
        visited = [False] * self.V  # Default all to false initially
        distances = [sys.maxint] * self.V  # All distances are defaulted to very high
        distances[start_node] = 0

        for j in range(self.V):
            # Get the minimum distance for the node
            min_node = self.min_distance(distances, visited)
            visited[min_node] = True

            for vertex in range(self.V):
                # Check to see if there is an edge. If there is, see if it is smaller (weight included)
                # than what is saved for the vertex. If there is no current distance, it will
                # be smaller
                if self.graph[min_node][vertex] > 0 and not visited[vertex] \
                         and distances[vertex] > distances[min_node] + self.graph[min_node][vertex]:

                    distances[vertex] = distances[min_node] + self.graph[min_node][vertex]

        return distances

            

class TestDijkstras(unittest.TestCase):

    def setup_basic_graph(self):
        g = Graph(9)
        g.graph = [
            [0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

        return g


    def readable(self, paths):
        dict = {}
        for index in range(len(paths)):
            dict[index] = paths[index]

        return dict

    def test_dijkstras(self):
        graph = self.setup_basic_graph()
        paths = graph.dijkstras(0)
        paths = self.readable(paths)
        self.assertEqual(paths[0], 0)
        self.assertEqual(paths[1], 4)
        self.assertEqual(paths[2], 12)
        self.assertEqual(paths[3], 19)
        self.assertEqual(paths[4], 21)
        self.assertEqual(paths[5], 11)
        self.assertEqual(paths[6], 9)
        self.assertEqual(paths[7], 8)
        self.assertEqual(paths[8], 14)


if __name__ == '__main__':
    unittest.main()

