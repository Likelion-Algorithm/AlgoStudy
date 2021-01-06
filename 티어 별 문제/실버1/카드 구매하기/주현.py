n = int(input())
pack = list(map(int, input().split()))
dp = [0]*(n+1)
answer = 0
for i in range(1,n+1):
    for j in range(i):
        if j == 0:
            temp = dp[j] + pack[i-j-1]
        else:
            temp = dp[j] + dp[i-j]
        if temp > dp[i]:
            dp[i] = temp
print(dp[-1])