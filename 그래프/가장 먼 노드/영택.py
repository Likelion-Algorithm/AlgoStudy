from collections import deque

def solution(n, edge):
    answer = 0

    G = {i:[] for i in range(1, n+1)}
    for v, u in edge: # 중복 간선 있으면 확인해줘야 함!
        G[v].append(u) 
        G[u].append(v)
    
    INF = -1
    visited = [INF for _ in range(n+1)]
    Q = deque([])
    Q.append([1,0]); visited[1] = 0

    while Q:
        u, d = Q.popleft()
        for v in G[u]:
            if visited[v] is INF:
                visited[v] = d+1
                Q.append([v, d+1])
        if not Q:
            max_distance = d
    
    for d in visited:
        if d == max_distance:
            answer += 1
    
    return answer
