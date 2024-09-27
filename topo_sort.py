
def topologicalSort(graph: dict) -> list:
    """
    A topological order is an ordering of vertices in a directed acyclic graph (DAG)
    such that for every directed edge u -> v, vertex u comes before v in the ordering
    """
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)
    
    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]