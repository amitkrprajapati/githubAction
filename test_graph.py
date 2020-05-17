import unittest

from Graph import Graph

graph = Graph(node_size=5, is_directed=False)


class GraphTest(unittest.TestCase):

    def test_graph_size(self):
        self.assertEqual(graph.node_size, 5)

    def test_graph_directed(self):
        self.assertEqual(graph.is_directed, False)


if __name__ == '__main__':
    unittest.main()
