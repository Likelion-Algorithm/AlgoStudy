num = int(input())
wine = [0,0]
dp = [0,0]
for i in range(num):
    wine.append(int(input()))
    dp.append(0)
for i in range(2,num+2):
    if i == 2:
        dp[i]=wine[i]
    else:
        dp[i] = max(dp[i-1],dp[i-3]+wine[i-1]+wine[i],dp[i-2]+wine[i])
print(dp[-1])


