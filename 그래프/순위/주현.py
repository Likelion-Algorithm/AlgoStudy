from collections import deque
def solution(n, results):
    answer = 0
    graph = [[0 for col in range(n)] for row in range(n)]
    for x, y in results:
        graph[x-1][y-1] = 1     #승리
        graph[y-1][x-1] = 2     #패배
    for i in range(n):
        if BFS(graph,i,1,n)+BFS(graph,i,2,n)==n-1:
            answer+=1
    return answer

def BFS(graph,start,vd,n):
    visit = 0
    bfs = deque([start])
    visited = [start]
    while bfs:
        loc = bfs.popleft()
        for i in range(n):
            if graph[loc][i]==vd and i not in visited:
                bfs.append(i)
                visited.append(i)
                visit+=1
    return visit
print(solution(5,[[4,3],[4,2],[3,2],[1,2],[2,5]]))