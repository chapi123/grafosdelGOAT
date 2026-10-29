Nodes = ["A", "B", "C", "D", "E", "F"]
Graphs = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def BFS(graph, start):
    visited = []
    queue = [start]
    visited.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


def DFS(graph, start):
    visited = set()

    def visit(node):
        visited.add(node)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)


BFS(Graphs, "C")
print()
DFS(Graphs, "C")