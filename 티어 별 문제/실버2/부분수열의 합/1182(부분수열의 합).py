import sys
from itertools import combinations

N,S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
answer = []
cnt = 0

for i in range(1,len(nums)+1):
    combi = list(combinations(nums, i))
    for j in combi:
        answer.append(sum(j))

for i in answer:
    if i == S:
        cnt += 1
print(cnt)

#통과
#문제를 잘 읽고 풀자아ㅏ아아!!!!!!