# 플로이드 와샬: 시작점과 끝점이 각 점을 거치는 경우와 거치지 않는 경우를 비교해 최단경로를 비교
# 더 작은 값이 존재하면 교체
import sys

N = int(sys.stdin.readline())
lst = []
visit = [0]*N
for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

def dfs(i):
    for j in range(len(lst[i])):
        if lst[i][j] == 1 and visit[j] == 0:
            visit[j] = 1
            dfs(j)

for i in range(N):
    dfs(i)
    for j in visit:
        print(j, end=' ')
    visit = [0]*N
    print()

#통과
#visit여부를 체크하는 방식 기억~