from collections import deque
from itertools import combinations
import copy
def bfs(BFS,GRAPH):
    virus = 0
    while BFS:
        x,y = BFS.popleft()
        virus+=1
        if x+1<N and GRAPH[x+1][y]==0:
            BFS.append([x+1,y])
            GRAPH[x+1][y]=2
        if x-1>=0 and GRAPH[x-1][y]==0:
            BFS.append([x-1,y])
            GRAPH[x-1][y]=2
        if y+1<M and GRAPH[x][y+1]==0:
            BFS.append([x,y+1])
            GRAPH[x][y+1]=2
        if y-1>=0 and GRAPH[x][y-1]==0:
            BFS.append([x,y-1])
            GRAPH[x][y-1]=2
    return virus

N, M = map(int , input().split())
graph = []
safe = []
ground = -3
bfsList = []
answer = 0

for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(M):
        if temp[j] == 2:
            bfsList.append([i,j])
    graph.append(temp)


for i in range(N):
    for j in range(M):
        if graph[i][j]==0 or graph[i][j]==2:
            ground +=1
            if graph[i][j]==0:
                safe.append([i,j])

brute = list(combinations(safe,3))

for i in brute:

    temp  = copy.deepcopy(graph)
    tempQueue = deque(copy.deepcopy(bfsList))
    for j in i:
        temp[j[0]][j[1]]=1
    안전지대 = ground - bfs(tempQueue,temp)
    if 안전지대 > answer:
        answer = 안전지대
    
print(answer)  
    
#브루트포스 + BFS알고리즘