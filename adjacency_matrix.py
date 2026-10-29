Nodes = ["A","B","C","D","E","F"]
Graphs = {"A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F"],
"D": ["B"], "E": ["B", "F"], "F": ["C", "E"]}

def adjacency_matrix(graph):
    matrix = [[0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]
    for i in range(len(Nodes)):
        for j in range(len(Nodes)):
            if Nodes[j] in graph[Nodes[i]]:
                matrix[i][j] = 1
    return matrix

def BFS(graph, start):
    visited = []
    queue = []
    visited.append(start)
    queue.append(start)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
            
BFS(Graphs, "C")
print()

def DFS(graph, start):
    visited = set()

    def visit(node):
        visited.add(node)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)

DFS(Graphs, "C")
