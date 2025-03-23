class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    uf = UnionFind(n)
    # Sort by cost first, and then prioritize rodovias over ferrovias if costs are equal
    edges.sort(key=lambda x: (x[2], not x[3]))  # True (rodovia) should be considered smaller than False (ferrovia) if costs are the same
    total_cost = 0
    edge_count = 0
    for u, v, cost, is_rodovia in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            total_cost += cost
            edge_count += 1
            if edge_count == n - 1:
                break
    return total_cost

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    index = 0
    N = int(data[index])
    index += 1
    F = int(data[index])
    index += 1
    R = int(data[index])
    index += 1
    
    edges = []
    
    # Read ferrovias
    for _ in range(F):
        A = int(data[index]) - 1
        index += 1
        B = int(data[index]) - 1
        index += 1
        C = int(data[index])
        index += 1
        edges.append((A, B, C, False))  # False denotes it's a ferrovia
    
    # Read rodovias
    for _ in range(R):
        I = int(data[index]) - 1
        index += 1
        J = int(data[index]) - 1
        index += 1
        K = int(data[index])
        index += 1
        edges.append((I, J, K, True))  # True denotes it's uma rodovia
    
    result = kruskal(N, edges)
    print(result)

if __name__ == "__main__":
    main()