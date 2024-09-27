from .topo_sort import topologicalSort

def scc(graph: dict) -> list:
    """
    Kosaraju's algorithm for finding strongly connected components (SCCs) in a directed graph.
    1. Compute a topological sort on the transposed graph  
    2. Perform DFS on the original graph in the order of the topological sort.

    Time complexity: O(V + E)
    """
    graph_t = {u: [] for u in graph}
    for u in graph:
        for v in graph[u]:
            graph_t[v].append(u)

    def dfs(u, components, n_comp):
        components[u] = n_comp
        for v in graph[u]:
            if components[v] is None:
                dfs(v, components, n_comp)
    
    order = topologicalSort(graph_t)
    components = [None] * len(graph)
    n_comp = 0
    for u in order:
        if components[u] is None:
            dfs(u, components, n_comp)
            n_comp += 1
    
    return components