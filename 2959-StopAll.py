import sys

MAXSIZE = 500

par = [i for i in range(MAXSIZE)]

def parent(u):
    if par[u] == u:
        return u
    return parent(par[u])

def scanff():
    a = 0
    c = sys.stdin.read(1)
    while c >= '0':
        a = a * 10 + (ord(c) - ord('0'))
        c = sys.stdin.read(1)
    return a

def main():
    n = scanff()
    m = scanff()
    p = scanff()

    for i in range(m):
        u = scanff()
        v = scanff()
        
        j = u
        while j != par[j]:
            j = par[j]

        k = v
        while k != par[k]:
            k = par[k]

        if j == k:
            continue

        par[j] = k

    for _ in range(p):
        u = scanff()
        v = scanff()

        u = parent(par[u])
        v = parent(par[v])

        if par[u] == par[v]:
            print("Lets que lets")
        else:
            print("Deu ruim")

if __name__ == "__main__":
    main()
