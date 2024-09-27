from collections import defaultdict

class DSU:
    """Disjoint Set Union data structure"""
    def __init__(self) -> None:
        self.parent = defaultdict(lambda: None)
        self.size = defaultdict(lambda: 1)

    def find(self, p):
        while self.parent[p] is not None:
            p = self.parent[p]
        return p

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        if self.size[u] < self.size[v]:
            u, v = v, u
        self.parent[v] = u
        self.size[u] += self.size[v]
    
    @property
    def roots(self):
        return set([self.find(k) for k in self.parent.keys()])