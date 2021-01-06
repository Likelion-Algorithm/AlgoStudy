N,M = map(int,input().split())
graph = [[0 for col in range(N+1)] for row in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
answer = 0
dfsStack = []
visited = [0]*(N+1)
for i in range(1,N+1):
    if not visited[i]:
        dfsStack.append(i)
        visited[i]=1
        answer+=1
        while dfsStack:
            loc = dfsStack.pop()
            for i in range(1,N+1):
                if graph[loc][i] and not visited[i]:
                    dfsStack.append(i)
                    visited[i]=1

print(answer)

#Python3 컴파일 시 실패. PyPy3 컴파일 시 성공.
#BFS와 DFS의 성능차에서 오는 것으로 추정