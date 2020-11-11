def dfs(n, computers, i, visited):
    visited[i] = True
    for j in range(n):
        if not visited[j] and computers[i][j] == 1:
            dfs(n, computers, j ,visited)

                

def solution(n, computers):
    answer =0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            answer+=1
            dfs(n, computers, i, visited)
    
    return answer