class Graph:
    def __init__(self, node_size, is_directed: bool):
        self.adjacent_list = []
        self.is_directed = is_directed
        self.node_size = node_size
        self.create_adjacent_list()

    def create_adjacent_list(self):
        for i in range(self.node_size):
            self.adjacent_list.append([])

    def add_node(self, u, v):
        self.adjacent_list[u].append(v)
        if not self.is_directed:
            self.adjacent_list[v].append(v)

    def print_graph(self):
        for u in range(self.node_size):
            if len(self.adjacent_list[u]):
                for v in self.adjacent_list[u]:
                    print(u, '->', v)
