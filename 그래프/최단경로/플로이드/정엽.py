import sys

n = int(sys.stdin.readline().strip())

graph = [[float('inf')]*n for i in range(n)]

repeat = int(sys.stdin.readline().strip())

for i in range(repeat):
    a,b,w = map(int,sys.stdin.readline().split())
    if graph[a-1][b-1]>w:
        graph[a-1][b-1] = w

for node in range(n):
    for start in range(n):
        for end in range(n):
            if start == end:
                graph[start][end] = 0
            graph[start][end] = min(graph[start][end],graph[start][node] + graph[node][end])

print(graph)
