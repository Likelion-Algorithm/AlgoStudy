import sys
import heapq
from collections import defaultdict
ANSWER = []
for i in range(int(sys.stdin.readline().strip())):
    dict1 = defaultdict(list)
    n, m, t = map(int,sys.stdin.readline().split())
    answer = {i + 1: float('inf') for i in range(n)}

    s, g, h = map(int,sys.stdin.readline().split())
    verify = [g,h]
    for i in range(m):
        a,b,d = map(int,sys.stdin.readline().split())
        if a not in dict1:
            dict1[a]={b:d}
        else:
            if b not in dict1[a]:
                dict1[a][b] = d
            else:
                dict1[a][b] = min(dict1[a][b],d)

        if b not in dict1:
            dict1[b] = {a:d}
        else:
            if a not in dict1[b]:
                dict1[b][a] = d
            else:
                dict1[b][a] = min(dict1[b][a],d)

    queue = []
    answer[s] = 0
    heapq.heappush(queue,[answer[s],s])
    while queue:
        weighted, node = heapq.heappop(queue)
        if weighted > answer[node] or dict1[node] == list:
            continue
        for x,y in dict1[node].items(): # y가 가중치
            if node in verify:
                if x in verify:
                    if answer[x] >= answer[node]+y:
                        answer[x] = float(answer[node])+y
                        heapq.heappush(queue,[answer[x],x])
                        continue
            if answer[x] > answer[node]+y:
                answer[x] = answer[node]+y
                heapq.heappush(queue,[answer[x],x])
            if answer[x] == answer[node]+y:
                if type(answer[x]) == float:
                    continue
                else:
                    answer[x] = answer[node]+y
    temp = []
    for i in range(t):
        a = int(sys.stdin.readline().strip())
        if (type(answer[a]) == float) & (answer[a] != float('inf')):
            temp.append(a)
    ANSWER.append(sorted(temp))

for i in ANSWER:
    print(*i)