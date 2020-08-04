import sys
from collections import defaultdict

n,k = map(int,sys.stdin.readline().split())

answer = defaultdict(list)
for i in range(1,k+1):
    answer[i] = float('-inf')

bags = defaultdict(list)

for i in range(n):
    w,v = map(int,sys.stdin.readline().split())
    if w not in bags:
        bags[w] = [v]
    else:
        bags[w].append(v)

for i in bags:
    bags[i].sort(reverse=True)

for i in range(1,k+1):
    if bags[i] == []:
        continue
    cnt = 0
    cnt_value = 0
    for j in bags[i]:
        cnt+=i
        cnt_value += j
        if (cnt > k) or (not answer[cnt]):
            continue
        if answer[cnt]<cnt_value:
            answer[cnt] = cnt_value
    for j in range(1,i):
        if (answer[j] == float('-inf')) or (i+j > k):
            continue
        if answer[i+j]<answer[i]+answer[j]:
            answer[i+j] = answer[i]+answer[j]

print(max(answer.items(),key = lambda x: x[1])[1])
print(answer)