def compara(a, b):
    return a[2] - b[2]

def componente(i):
    if i == p[i]:
        return i
    return componente(p[i])

def kruskal(c):
    ans = 0
    for i in range(c):
        v = componente(g[i][0])
        u = componente(g[i][1])
        if v != u:
            p[v] = p[u]
            ans += g[i][2]
    return ans

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    g = []
    p = [i for i in range(m + 1)]

    for _ in range(n):
        u, v, w = map(int, input().split())
        g.append((u, v, w))

    g.sort(key=lambda x: x[2])

    print(kruskal(n))
