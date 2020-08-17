import heapq,sys
T = int(input())
length = 100000
point=[]

def destination(graph,s,g,h,n,m):
    pathList = list()
    queue = list()
    answer = [False]*(n+1)
    INF = length*m
    for i in range(n+1):
        pathList.append(INF)
    pathList[s]=0
    heapq.heappush(queue, [0,s])
    while queue:
        loc = heapq.heappop(queue)[1]
        for w, v in graph[loc]:
            if pathList[v]>=pathList[loc]+w:
                pathList[v] = pathList[loc]+w
                if (loc==g and v==h) or (loc==h and v==g):
                    answer[v]=True
                elif answer[loc]==True:
                    answer[v]=True
                elif pathList[v]!=pathList[loc]+w:
                    answer[v]=False
                heapq.heappush(queue, [pathList[v],v])
    return answer
for i in range(T):
    n,m,t = map(int, input().split())
    s,g,h = map(int, input().split())
    graph = {i:[] for i in range(1,n+1)}
    for j in range(m):
        a,b,d = map(int, input().split())
        graph[a].append([d,b])
        graph[b].append([d,a])
    temp = destination(graph,s,g,h,n,m)[::]
    temp2 = []
    for k in range(t):
        num = int(input())
        if temp[num]:
            temp2.append(num)
    point.append(temp2)
for i in range(T):
    point[i].sort()
    for j in range(len(point[i])):
        print(point[i][j],end=' ')
    print()
        