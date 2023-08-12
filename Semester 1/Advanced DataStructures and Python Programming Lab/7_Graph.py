class WeightedGraph:
    def __init__(self):
        self.graph = {}
        self.vertices = set()

    def add_edge(self, source, destination, weight):
        self.vertices.add(source)
        self.vertices.add(destination)

        if source not in self.graph:
            self.graph[source] = {}
        self.graph[source][destination] = weight

        if destination not in self.graph:
            self.graph[destination] = {}
        self.graph[destination][source] = weight

    def display_adjacency_matrix(self):
        vertices = sorted(list(self.vertices))
        n = len(vertices)
        adj_matrix = [[0] * n for _ in range(n)]

        for i, vertex in enumerate(vertices):
            adj_list = self.graph.get(vertex, {})
            for adj_vertex, weight in adj_list.items():
                j = vertices.index(adj_vertex)
                adj_matrix[i][j] = weight

        print("Vertices:", ", ".join(vertices))
        for i in range(n):
            print(f"Adjacent to {vertices[i]}:", [vertices[j] for j in range(n) if adj_matrix[i][j] != 0])

        print("\nAdjacency Matrix:")
        for row in adj_matrix:
            row_str = " ".join(str(val) if val != 0 else 'x' for val in row)
            print(row_str)


if __name__ == "__main__":
    graph = WeightedGraph()

    print("Enter the (source, destination, weight) and enter halt to finish the entry: ") 
    while True:
        input_str = input() #eg., (a,b,8)
        if input_str.lower() == "halt":
            break

        try:
            source, destination, weight = input_str.strip('()').split(',')
            graph.add_edge(source.strip(), destination.strip(), int(weight.strip()))
        except ValueError:
            print("Invalid input format. Please enter in the format (source, destination, weight)")

    graph.display_adjacency_matrix()
