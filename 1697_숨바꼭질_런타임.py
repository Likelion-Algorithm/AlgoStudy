from collections import deque
import  sys


deque = deque()

N, K = map(int, sys.stdin.readline().split())

dx = [-1, 1, 2 ] #직선 위에서 움직임
if N > K:
    visited = [0] * N
else:
    visited = [0] * K

deque.append(N)

while deque:
    a = deque.popleft()
    if K in deque :
        print(visited[K+1])
        break

    for i in range(3):
        if i == 2:
            try:
                x = dx[i]*a
                if visited[x+1] == 0:
                    deque.append(x)
                    visited[x+1] = visited[a+1] + 1

            except IndexError:
                for i in range(x - len(visited)+2):
                    visited.append(0)
                if visited[x + 1] == 0:
                    deque.append(x)
                    visited[x + 1] = visited[a + 1] + 1


        else:
            try:
                x = dx[i] + a
                if visited[x+1] == 0:
                    deque.append(x)
                    visited[x+1] = visited[a+1] + 1
            except IndexError:
                    for i in range(x - len(visited) + 2):
                        visited.append(0)
                    if visited[x + 1] == 0:
                        deque.append(x)
                        visited[x + 1] = visited[a + 1] + 1




