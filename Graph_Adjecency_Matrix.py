# Implementation of Graph using Adjacency Matrix (for undirected graph)
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    # Add edge
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1   # For undirected graph

    # Display graph
    def display(self):
        for row in self.matrix:
            print(row)

# Example usage
g = Graph(4)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("Adjacency Matrix:")
g.display()