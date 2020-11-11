from collections import deque

def solution(n, computers):
    answer = 0
    bfsDeque = deque([])
    visited = []
    for computer in range(n):
        if computer not in visited:
            bfsDeque.append(computer)
            while bfsDeque:         #BFS실시 후 answer 증가
                temp = bfsDeque.popleft()
                visited.append(temp)
                for i in range(n):
                    if computers[temp][i]==1 and i not in visited:
                        bfsDeque.append(i)
            answer+=1

    return answer