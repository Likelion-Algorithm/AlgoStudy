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