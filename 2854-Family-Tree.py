class TreeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def dfs(vertex):
    vis[vertex] = True
    for i in range(1, m + 1):
        if adj[vertex][i]:
            if not vis[i]:
                dfs(i)

def push(tree, string):
    global idx
    if not tree:
        tree = TreeNode(string)
        tree.id = idx + 1
        idx += 1
    elif tree.name > string:
        tree.left = push(tree.left, string)
    elif tree.name < string:
        tree.right = push(tree.right, string)
    return tree

def find(tree, string):
    if not tree:
        return -1
    if tree.name > string:
        return find(tree.left, string)
    elif tree.name < string:
        return find(tree.right, string)
    else:
        return tree.id

MAXSIZE = 310
true = 1
false = 0

vis = [False] * MAXSIZE
adj = [[False] * MAXSIZE for _ in range(MAXSIZE)]

idx = 0
m, n = map(int, input().split())

arvore = None

for _ in range(n):
    name1, conex, name2 = input().split()
    arvore = push(arvore, name1)
    arvore = push(arvore, name2)

    u = find(arvore, name1)
    v = find(arvore, name2)

    adj[u][v] = adj[v][u] = True

ans = 0
for i in range(1, m + 1):
    if not vis[i]:
        ans += 1
        dfs(i)

print(ans)
