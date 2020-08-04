# # def dijk(graph, start, num):
#     answer = collections.defaultdict(list)
#     answer = {i:float('inf') for i in graph}
#     answer[start] = num
#
#     QUEUE = []
#     heapq.heappush(QUEUE,[answer[start],start])
#
#     while QUEUE:
#         weighted, node = heapq.heappop(QUEUE)
#         if weighted > answer[node]:
#             continue
#         for x,y in graph[node].items():
#             if answer[x] > answer[node] + y:
#                 answer[x] = answer[node]+y
#                 heapq.heappush(QUEUE,[answer[x],x])
#
#     print(answer)






















import sys
import heapq
import collections
import time

v,e = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline().strip())

graph = collections.defaultdict(list)

for i in range(e):
    a,b,w = map(int,sys.stdin.readline().split())
    if a not in graph:
        graph[a] = {b:w}
    else:
        if b not in graph[a]:
            graph[a][b] = w
        else:
            if graph[a][b] > w:
                graph[a][b] = w

# dijk(graph,start,0)

answer = {i:float('inf') for i in range(1,v+1)}
answer[start] = 0

QUEUE = []
heapq.heappush(QUEUE,[answer[start],start])

while QUEUE:
    weighted, node = heapq.heappop(QUEUE)
    if weighted > answer[node] or graph[node] == []:
        continue
    for x,y in graph[node].items():
        if answer[x] > answer[node] + y:
            answer[x] = answer[node]+y
            heapq.heappush(QUEUE,[answer[x],x])

for i in sorted(answer.items(),key = lambda x:x[0]):
    print([i[1],'INF'][i[1]==float('inf')])