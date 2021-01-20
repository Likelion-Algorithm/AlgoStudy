from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
for node in range(n):
    queue = deque([node])
    temp = [0]*n
    while queue:
        loc = queue.popleft()
        for dest in range(n):
            if graph[loc][dest] and temp[dest] == 0:
                temp[dest] = 1
                queue.append(dest)
    for i in temp:
        print(i , end=' ')
    print()