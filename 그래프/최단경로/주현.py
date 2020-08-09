import heapq,sys

V, E = map(int, sys.stdin.readline().strip().split())
start = int(sys.stdin.readline())
graph = {i:[] for i in range(1, V+1)}
pathList = list()
queue = list()
INF = V*11
for i in range(V+1):
    pathList.append(INF)
pathList[start]=0
for i in range(E):
    u,v,w = map(int,sys.stdin.readline().strip().split())
    graph[u].append([w,v])
heapq.heappush(queue, [0,start])
while queue:
    loc = heapq.heappop(queue)[1]
    for w, v in graph[loc]:
        if pathList[v]>pathList[loc]+w:
            pathList[v] = pathList[loc]+w
            heapq.heappush(queue, [pathList[v],v])
    
    
for i in range(1,V+1):
    if pathList[i]==INF:
        print('INF')
    else:
        print(pathList[i])