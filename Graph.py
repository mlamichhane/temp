from collections import deque

# Implementation of Graph data structure (for undirected graph)
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1) 

    def display(self):
        for vertex in self.adjacency_list:
            print(f"{vertex} -> {self.adjacency_list[vertex]}")

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        print("BFS Traversal:", end=" ")
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(neighbor 
                             for neighbor in self.adjacency_list[vertex] 
                             if neighbor not in visited
                             )
        print()

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
            print("DFS Traversal:", end=" ")

        if start not in visited:
            print(start, end=" ")
            visited.add(start)
            for neighbor in self.adjacency_list[start]:
                if neighbor not in visited:
                    self.dfs(neighbor, visited)

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'E')
    g.add_edge('E', 'F')

    g.display()

    g.bfs('A')
    g.dfs('A')

    print()
