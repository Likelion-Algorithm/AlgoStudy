from collections import deque
def solution(n, edge):
    answer = 0
    graph = dict()                  #그래프를 인접행렬과 인접 리스트로 표현할때의 성능차이가 매우 큼
    for i in range(n):
        graph.setdefault(i,[])
    for x,y in edge:
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)
    BFS = deque([0])
    visited = [1]*n
    depth = [0]*n
    visited[0]=0
    while BFS:                      #depth를 기록하는  BFS실시
        loc = BFS.popleft()
        for i in graph[loc]:
            if visited[i]:
                BFS.append(i)
                visited[i]=0
                depth[i]=depth[loc]+1
    answer = depth.count(max(depth)) #depth가 가장 깊은 노드의 개수

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))