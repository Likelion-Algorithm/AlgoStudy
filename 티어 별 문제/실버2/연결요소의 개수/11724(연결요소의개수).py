import sys

N,M = map(int, sys.stdin.readline().split())
checker = [False]*(N+1)
nodes = [[] for _ in range(N+1)]
cnt = 0

for _ in range(M):
    num1, num2 = map(int, sys.stdin.readline().split())
    nodes[num1].append(num2)
    nodes[num2].append(num1)

def bfs(num):
    tmp = [num]
    checker[num] == True

    while tmp:
        target = tmp.pop(0)
        for i in nodes[target]:
            if checker[i] == False:
                tmp.append(i)
                checker[i] == True

for i in range(1, N+1):
    if checker[i] == False:
        bfs(i)
        cnt += 1

print (cnt)

#다른사람코드 참조, 시간초과뜸 ㅠ
