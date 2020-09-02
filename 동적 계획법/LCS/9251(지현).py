import sys

a = str(sys.stdin.readline().rstrip())
b = str(sys.stdin.readline().rstrip())

graph = []

for _ in range(len(a)+1):
    graph.append([0]*(len(b)+1))

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):

        if a[i-1] == b[j-1]:
            graph[i][j] = graph[i-1][j-1] + 1
        else:
            graph[i][j] = max(graph[i-1][j], graph[i][j-1])

print(graph[len(a)][len(b)])





