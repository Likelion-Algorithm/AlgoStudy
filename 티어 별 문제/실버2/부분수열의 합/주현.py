from itertools import combinations
N ,S = map(int,input().split())
sequence = list(map(int,input().split()))
answer = 0
for i in range(N):
    part_sequence = combinations(sequence,i+1)
    for j in part_sequence:
        if sum(j)==S:
            answer+=1
print(answer)

#브루트포스 (1<=N<=20)