from collections import deque
T = int(input())
controll = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
answer = [0]*T
for test in range(T):
    N = int(input())
    graph = [[0 for col in range(N)] for row in range(N)]
    queue = deque([])
    start = list(map(int, input().split()))
    queue.append(start)
    end = list(map(int, input().split()))
    while queue:
        loc = queue.popleft()
        depth = graph[loc[0]][loc[1]]
        if [loc[0], loc[1]] == end:
            answer[test] = depth
            break
        for x,y in controll:
            if (loc[0]+x>=0 and loc[0]+x<N) and (loc[1]+y>=0 and loc[1]+y<N)  :
                if graph[loc[0]+x][loc[1]+y] > depth + 1 or graph[loc[0]+x][loc[1]+y]==0 and [loc[0]+x,loc[1]+y] != start:
                    queue.append([loc[0]+x,loc[1]+y])
                    graph[loc[0]+x][loc[1]+y] = depth + 1
for i in answer:            
    print(i)

#BFS, PyPy3시 성공