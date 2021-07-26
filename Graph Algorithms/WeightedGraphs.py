import unittest
import sys


class Graph:
    def __init__(self, vertices):
        self.graph = []
        self.v = vertices

    def add_edge(self, node_t, node_f, weight):
        self.graph.append([node_t, node_f, weight])

    def find(self, parent_node, i):
        if parent_node[i] == i:
            return i
        else:
            return self.find(parent_node, parent_node[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1


class DirectedGraph(Graph):
    def __init__(self, vertices):
        Graph.__init__(self, vertices)


class UndirectedGraph(Graph):
    def __init__(self, vertices):
        Graph.__init__(self, vertices)

    def kruskal(self):
        """
            Return MST using kruskal's algo
            O(E log V)
        :return:
        """
        i = 0
        j = 0
        result_arr = []

        # Sort the graph based on weight
        sorted_graph = sorted(self.graph, key=lambda item: item[2])

        parent = [v for v in range(self.v)]
        rank = [0 for v in range(self.v)]

        while j < self.v - 1:
            # Pop out min items (if not already included in our MST
            u, v, w = sorted_graph[i]

            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # Check for cycles. If no cycle add (we know its the min weight already)
            if x != y:
                j += 1
                result_arr.append([u, v, w])
                self.union(parent, rank, x, y)

        return result_arr

    def min_weight(self, key, set):

        # Initilaize min value
        min = sys.maxint
        min_index = None

        for v in range(self.v):
            if key[v] < min and set[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def prims(self):
        """
        1) Create a set mstSet that keeps track of vertices already included in MST.
        2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE.
            Assign key value as 0 for the first vertex so that it is picked first.
        3) While mstSet doesn't include all vertices
            a) Pick a vertex u which is not there in mstSet and has minimum key value.
            b) Include u to mstSet.
            c) Update key value of all adjacent vertices of u. To update the key values, iterate through all
            adjacent vertices. For every adjacent vertex v, if weight of edge u-v is less than the previous key value of
            v, update the key value as weight of u-v

        Time complexity: O(V^2)
        Space complexity: O(V^3)
        :return:
        """
        # Init to the largest value
        keys = [sys.maxint] * self.v
        parent = [None] * self.v

        keys[0] = 0
        set = [False] * self.v
        parent[0] = -1  # 0 is always root

        path_and_weight = []  # In the form of (u, v, w)

        for i in range(self.v):
            # Find the min weight from all weights which are not visited
            min = self.min_weight(keys, set)
            # Denote as visited
            set[min] = True

            for vertex in range(self.v):
                if keys[vertex] > self.graph[min][vertex] > 0 and not set[vertex]:
                    keys[vertex] = self.graph[min][vertex]
                    parent[vertex] = min
                    path_and_weight.append((min, vertex, self.graph[vertex][parent[vertex]]))

        return path_and_weight


class Test(unittest.TestCase):
    def test_kruskal(self):
        g = UndirectedGraph(4)
        g.add_edge(0, 1, 10)
        g.add_edge(0, 2, 6)
        g.add_edge(0, 3, 5)
        g.add_edge(1, 3, 15)
        g.add_edge(2, 3, 4)

        krusk = g.kruskal()
        valid = [
            [2, 3, 4],
            [0, 3, 5],
            [0, 1, 10]
        ]
        self.assertEqual(krusk, valid)

    def test_prims(self):
        g = UndirectedGraph(5)
        g.graph = [
            [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]
        ]

        mst = g.prims()
        self.assertEqual(mst, [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 4, 5)])


