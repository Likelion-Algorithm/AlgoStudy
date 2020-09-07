num = int(input())
wine = [0,0,0]
dp = [[0 for col in range(num+3)] for row in range(num+3)]
for i in range(num):
    wine.append(int(input()))
for i in range(3,num+3):
    for j in range(3,num+3):
        if j==3:
            dp[i][j] = max(wine[:i+1])
        else:
            dp[i][j]= max(dp[i-1][j],dp[i-2][j-1]+wine[i],dp[i-3][j-2]+wine[i]+wine[i-1])
print(dp[-1][-1])

#백준 메모리 초과.