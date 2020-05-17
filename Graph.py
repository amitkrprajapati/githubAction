from queue import Queue

class Graph:
    def __init__(self, node_size, is_directed: bool):
        self.adjacent_list = []
        self.is_directed = is_directed
        self.node_size = node_size
        self.create_adjacent_list()

    def create_adjacent_list(self):
        self.adjacent_list.append([])
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

    def dfsUtil(self, u, vis, order: list):
        vis[u] = 1
        order.append(u)
        for v in self.adjacent_list[u]:
            if not vis[v]:
                self.dfsUtil(v, vis, order)

    def dfs(self, u):
        vis = [0] * (self.node_size + 1)
        order = []
        self.dfsUtil(u, vis, order)
        return order

    def bfs(self, u):
        q = Queue()
        vis = [0] * (self.node_size + 1)
        order = []
        q.put(u)
        vis[u] = 1
        while not q.empty():
            u = q.get()
            print(u)
            order.append(u)
            for v in self.adjacent_list[u]:
                if not vis[v]:
                    vis[v] = 1
                    q.put(v)
        return order
