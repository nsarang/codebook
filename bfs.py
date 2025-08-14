from collections import deque

def bfs(graph, start):
    """Breadth-First Search (BFS)"""
    visited = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        level = visited[node]
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = level + 1
                queue.append(neighbor)
