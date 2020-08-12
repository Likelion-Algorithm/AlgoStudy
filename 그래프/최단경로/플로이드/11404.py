import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

path = []

for _ in range(n):
    path.append(['INF']*n)  #path 리스트를 먼저 'INF'로 채워주기

for i in range(n):
    for j in range(n):
        if i == j:
            path[i][j] = 0  #자기자신으로 가는 경로는 없으니 0으로 바꿔줌

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    
    if path[a-1][b-1] == 'INF':
        path[a-1][b-1] = c   # 입력값 중 경로에 해당하는 비용이 입력되면 'INF'를 비용으로 바꿔줌
    else:
        if path[a-1][b-1] > c: # 경로가 여려개가 입력되는 경우는 기존 값과 비교해 새로운 값이 더 작을 경우 새로운 값으로 바꿔줌
            path[a-1][b-1] = c

for k in range(n): 
    for i in range(n):
        for j in range(n):
            
            if path[i][j] == 'INF': # 'INF'인 경우
                if path[i][k] != 'INF' and path[k][j] != 'INF': # 경유경로를 포함하는 값이 모두 'INF'가 아닌 경우 -> 경유경로 값으로 바꿔줌
                    path[i][j] = path[i][k] + path[k][j]
                else: #경유경로에 'INF'를 포함하는 경우에는 어짜피 더해도 'INF'가 나오므로 pass
                   pass
            else: # 'INF'가 아닌 경우
                if path[i][k] != 'INF' and path[k][j] != 'INF': # 경유경로를 포함하는 값이 모두 'INF'가 아닌 경우
                    if path[i][j] > path[i][k] + path[k][j]:
                        path[i][j] = path[i][k] + path[k][j]  #-> 기존의 값이 경유경로 값보다 클 경우 경유경로 값으로 바꿔줌




            
for i in path:
    for j in i:
        if j == 'INF': # i에서 j로 갈 수 없는 경우는 'INF'로 남아있으므로 문제 조건에 맞게 0으로 바꿔줌
            j = 0
        print(j, end=' ')
    print()
    

    


