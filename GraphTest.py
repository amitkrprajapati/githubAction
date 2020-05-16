import unittest

from Graph import Graph


class GraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(node_size=5, is_directed=False)

    def test_graph_size(self):
        self.assertEqual(self.graph.node_size, 5)


if __name__ == '__main__':
    unittest.main()
