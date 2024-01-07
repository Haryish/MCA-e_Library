import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        dfs_order = []

        def dfs_recursive(node):
            visited.add(node)
            dfs_order.append(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return dfs_order

def visualize_dfs(graph, dfs_order):
    G = nx.DiGraph()
    for node, neighbors in graph.graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    labels = {node: node for node in G.nodes()}

    node_colors = ['blue' if node in dfs_order else 'gray' for node in G.nodes()]

    nx.draw(G, pos, labels=labels, node_color=node_colors, with_labels=True, arrows=True)
    plt.show()

# Example usage:
g = Graph()
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3)
g.add_edge(3, 4)
g.add_edge(4,3)

start_node = 2
dfs_order = g.dfs(start_node)
print("DFS starting from vertex 2:")
print(dfs_order)

visualize_dfs(g, dfs_order)
