import matplotlib.pyplot as plt
import networkx as nx

def bfs(graph, start_node):
    visited = set()
    queue = [start_node]
    visited.add(start_node)
    bfs_order = [start_node]

    while queue:
        node = queue.pop(0)

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                bfs_order.append(neighbor)

    return bfs_order

G = nx.DiGraph()

G.add_edge(0, 1)
G.add_edge(0, 3)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 1)
G.add_edge(2, 3)
G.add_edge(3, 3)

start_node = 2
bfs_order = bfs(G, start_node)
print("BFS starting from vertex 2:", bfs_order)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=600)
plt.title("BFS Visualization")
plt.show()
