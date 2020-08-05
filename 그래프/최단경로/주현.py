import heapq,sys
V, E = map(int, sys.stdin.readline().strip().split())
start = int(sys.stdin.readline())
graph = []
pathList = list()
visited = list()
point = list()
queue = list()
INF = V*11
for i in range(V+1):
    graph.append({})
    pathList.append(INF)
for i in range(1,V+1):
    point.append(i)
pathList[start]=0
for i in range(E):
    u,v,w = map(int,sys.stdin.readline().strip().split())
    if v not in graph[u] or graph[u][v]>w:
        graph[u][v]=w

while point:
    temp =INF
    for i in point:
        if temp>=pathList[i]:
            temp = pathList[i]
            loc = i
    for i in graph[loc].keys():
        heapq.heappush(queue,(graph[loc][i], i))
    for i in range(len(queue)):
        i = heapq.heappop(queue)
        if pathList[i[1]]>pathList[loc]+i[0]:
            pathList[i[1]] = pathList[loc]+i[0]
    visited.append(point.pop(point.index(loc)))
    
for i in range(1,len(pathList)):
    if pathList[i]==INF:
        print('INF')
    else:
        print(pathList[i])

