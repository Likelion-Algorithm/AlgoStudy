import sys

n, k = map(int, sys.stdin.readline().split())
tmp = []
dp = [0] * (k + 1)
dp[0] = 1

for _ in range(n):
    tmp.append(int(sys.stdin.readline()))
tmp.sort()

for price in tmp:
    for i in range(price, k + 1):
        dp[i] += dp[i - price]

print(dp[k])