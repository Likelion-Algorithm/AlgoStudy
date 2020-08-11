import sys
from collections import deque
M,N = map(int,sys.stdin.readline().split())
graph = list()
q= deque([])
for i in range(N+2):      #그래프 생성
    if i==0:
        graph.append([0 for col in range(M+2)])
    elif i==N+1:
        graph.append([0 for col in range(M+2)])
    else:
        graph.append(list(map(int, sys.stdin.readline().split())))
        graph[i].insert(0,0)
        graph[i].insert(M+2,0)
        for j in range(M+1):
            if graph[i][j]==1:
                q.append([i, j])

while q:                  #BFS탐색을 실시하며 깊이를 기록한다.
    i,j = q.popleft()
    if i!=0 and j!=0 and i!=N+1 and j!=M+1:
        temp=graph[i][j]
        if graph[i-1][j]==0:
            graph[i-1][j]=graph[i][j]+1
            q.append([i-1,j])
        if graph[i][j-1]==0:
            graph[i][j-1]=graph[i][j]+1
            q.append([i,j-1])
        if graph[i][j+1]==0:
            graph[i][j+1]=graph[i][j]+1
            q.append([i,j+1])
        if graph[i+1][j]==0:
            graph[i+1][j]=graph[i][j]+1
            q.append([i+1,j])

tomato=True
for i in range(1,len(graph)-1):
    if 0 in graph[i][1:M]:
        tomato=False
        break
    
if tomato:                 #그래프에 0이 있으면 -1 출력, 없으면 BFS깊이를 출력
    print(temp-1)
else:
    print(-1)