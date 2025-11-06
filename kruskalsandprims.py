# Minimum Spanning Tree using Kruskal's and Prim's Algorithm

# ---------- Graph Representation ----------
# Let’s assume the college has 4 departments:
# 0 - Computer Dept
# 1 - Mechanical Dept
# 2 - Civil Dept
# 3 - Electrical Dept
# Distance between departments is shown in adjacency matrix

INF = 9999
graph = [
    [0, 10, 6, 5],
    [10, 0, INF, 15],
    [6, INF, 0, 4],
    [5, 15, 4, 0]
]

# ---------- Kruskal’s Algorithm ----------
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i, j):
        a = self.find(i)
        b = self.find(j)
        if a != b:
            self.parent[a] = b

def kruskal(graph):
    edges = []
    n = len(graph)
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] != 0 and graph[i][j] != INF:
                edges.append((graph[i][j], i, j))

    edges.sort()  # sort by weight
    ds = DisjointSet(n)
    mst = []
    total = 0

    for w, u, v in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
            total += w

    print("\nMST using Kruskal's Algorithm:")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")
    print("Total Minimum Cost:", total)


# ---------- Prim’s Algorithm ----------
def prim(graph):
    n = len(graph)
    selected = [False] * n
    selected[0] = True  # Start from node 0
    edges = 0
    total = 0

    print("\nMST using Prim's Algorithm:")
    while edges < n - 1:
        minimum = INF
        x = y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if (not selected[j]) and graph[i][j] != 0 and graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x, y = i, j
        print(f"{x} -- {y} == {graph[x][y]}")
        total += graph[x][y]
        selected[y] = True
        edges += 1

    print("Total Minimum Cost:", total)


# ---------- Main ----------
kruskal(graph)
prim(graph)
