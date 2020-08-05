import heapq,sys
V, E = map(int, sys.stdin.readline().strip().split())
start = int(sys.stdin.readline())
graph = {}
pathList = list()
queue = list()
INF = V*11
for i in range(V+1):
    pathList.append(INF)
pathList[start]=0
for i in range(E):
    u,v,w = map(int,sys.stdin.readline().strip().split())
    graph[u]=[w,v]
heapq.heappush(queue, graph[start])
while queue:
    loc = heapq.heappop(queue)
    for i in range(len(graph[loc[1]])):
        heapq.heappush(queue, graph[loc[1]][i])
        if pathList[graph[loc[1]][i][1]]>pathList[loc[1]]+loc[0]:
            pathList[graph[loc[1]][i][1]] = pathList[loc[1]]+loc[0]
print(pathList)

    
    
for i in range(1,len(pathList)):
    if pathList[i]==INF:
        print('INF')
    else:
        print(pathList[i])

