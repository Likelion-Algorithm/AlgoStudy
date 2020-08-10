size = int(input())
num = int(input())
INF = 100001
graph = [[INF for row in range(size+1)] for col in range(size+1)]
for exe in range(num):
    i, j, cost =  map(int, input().split())
    if graph[i][j]==0 or cost < graph[i][j] :
        graph[i][j] = cost

for i in range(1,size+1):
    for j in range(1,size+1):
        for k in range(1,size+1):
            if i!=j and i!=k:
                if graph[i][j]> graph[k][j]+graph[i][k]:
                    graph[i][j] = graph[k][j]+graph[i][k]
print(graph)