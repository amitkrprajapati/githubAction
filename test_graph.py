import unittest

from Graph import Graph

graph = Graph(node_size=6, is_directed=False)

# 1--6--3
# | /|
# |/ |
# 4--5--2
graph.add_node(1, 6)
graph.add_node(6, 3)
graph.add_node(1, 4)
graph.add_node(6, 5)
graph.add_node(6, 4)
graph.add_node(4, 5)
graph.add_node(5, 2)


class GraphTest(unittest.TestCase):

    def test_graph_size(self):
        self.assertEqual(graph.node_size, 6)

    def test_graph_directed(self):
        self.assertEqual(graph.is_directed, False)

    def test_dfs(self):
        expected = [1, 6, 3, 5, 2, 4]
        actual = graph.dfs(1)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
