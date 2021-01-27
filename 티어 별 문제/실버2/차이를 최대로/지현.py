import sys
import itertools

N = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))
tmp_ = itertools.permutations(tmp, N)
answer = []

for item in tmp_:
    cnt = 0
    for j in range(len(item)-1):
        cnt += abs(item[j]-item[j+1])
    answer.append(cnt)

print(max(answer))

# 통과
# 순열: 서로 다른 n개 중 r개를 골라 순서를 정해 나열 - (a,b)와 (b,a)는 다른것
# import itertools 한 후 itertools.permutations(나열하고자 하는 배열, r)
# 조합: 서로 다른 n개 중 r를 골라 그룹을 만드는 것 - 그룹이므로 구성의 순서는 상관 없으므로 (a,b)와 (b,a)는 같은 것
# import itertools 후 itertools.combinations(배열, r)