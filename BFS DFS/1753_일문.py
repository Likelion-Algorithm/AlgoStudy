import sys
INF = 9999
V, E = map(int, sys.stdin.readline().split())
K= int(sys.stdin.readline())
graph_list = [[] for _ in range(V+1)]
visited = [INF]*(V+1)

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph_list[u].append([w,v])

def dijk():
    queue = []
    visited[K] = 0
    queue.append((0,K))
    queue = sorted(queue)
    while queue:
        w, v = queue.pop()
        if visited[v] < w:
            continue

dijk()

