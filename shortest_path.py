import sys

v, e = map(int, sys.stdin.readline().split())
start = int(input()) - 1
graph = []
D = []

for i in range (e):
    _from, _to, w = map(int, sys.stdin.readline().split())
    graph.append([_from-1, _to-1, w])

for i in range (v):
    D.append(11)

for i in range (v): # D[0] ~ D[v-1] 구하기 (D[i] = start부터 i까지의 최단거리)
    for j in range (e): # graph[0] ~ graph[e-1]까지 확인
        if ( i == start ):
            D[i] = 0
        
        if (graph[j][1] == i):
            # start에서 구하는 값까지 바로 가는 경우 
            if (graph[j][0] == start):
                D[i] = min(D[i], graph[j][2])
            # N ~ 구하는 값까지 가는 경우 (D[N] + 현재 체크하는 값의 가중치)
            else:
                D[i] = min(D[i], D[graph[j][0]] + graph[j][2])


for i in range (v):
    if(D[i] == 11):
        print('INF')
    else:
        print(D[i])


