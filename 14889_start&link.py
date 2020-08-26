import sys
from itertools import combinations

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
compare = list()
start_link = list(range(N))
people = list(combinations(start_link, N // 2))

for team in people:
    start = list(team)
    link = list(set(temp)-set(team))

start_compare = list()
link_compare = list()

def dfs(graph):
    for i in start:
        for j in start:
            if i < j:
                start_compare.append(matrix[i][j] + matrix[j][i])
    for i in link:
        for j in link:
            if i < j:
                link_compare.append(matrix[i][j] + matrix[j][i])

sol = list()
dfs(matrix)


for i in range(len(compare)-1):
    if len(sol) == 0:
        sol.append(compare[i] - compare[i+1])
    else:
        if i+1 < len(compare):
            a = sol.pop()
            if a > compare[i] - compare[i+1]:
                sol.append(a)
            else:
                sol.append(compare[i] - compare[i+1])

# 문제점 : 가장 작은 차이를 구하는 것을 집중하는 나머지 한 사람이 두 팀에 들어가는 경우를 배제하지 못했다.
# 이를 배제하려면 처음부터 따로 사람을 뽑아줘야 했다.

print(compare)
print(sol)
# print(abs(compare[0] - compare[1]))
