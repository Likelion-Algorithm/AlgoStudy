import sys
N = int(sys.stdin.readline().strip())
sequence = list(map(int, sys.stdin.readline().split()))
sol_list = list()
len_list = list()
for i in range(N):
    sol_list.append(sequence[i])
    for j in range(N):
        if i >= j :
            continue
        else:
            if sequence[j] <= sol_list[len(sol_list)-1]:
                continue
            else:
                sol_list.append(sequence[j])
    len_list.append(len(sol_list))
    sol_list.clear()
print(max(len_list))

# 다음 반례를 풀지 못해 틀림
# 즉, 첫 1, 4,5를 잡아낸 후 다음 2 3 4 5를 잡아내지 못하는 문제점이 있었다.
# 7
# 1 4 5 2 3 4 5


import sys
n = int(sys.stdin.readline().strip())
seqeunce = list(map(int, sys.stdin.readline().split()))
dp = [0 for i in range(n)]

for i in range(n): #수열의 크기  0, 1, 2,3 , ... n-1까지 점점 늘어나는 형태
    for j in range(i): # j는 반드시 i보다 작다.
        if seqeunce[i] > seqeunce[j] and dp[i] < dp[j]: # 증가수열이고 마지막 원소의 dp에 0이 저장되어 있을 때, i길이의 수열 맨 마지막 원소(sequence[i])와 나머지 원소 비교
            dp[i] = dp[j]
    dp[i] += 1 #동기화 했다는 것은 증가수열이라는 말이므로 길이+1해준다.
print(max(dp))