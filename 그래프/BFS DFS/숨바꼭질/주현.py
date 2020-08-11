start, end = map(int,input().split())
dpList = []                                 #dp 차트생성
for i in range(start+1,0,-1):
    dpList.append(i-1)
for i in range(start+1,end+2):              #dp[n]= min(dp[n-1]+1,dp[n+1]+1,dp[n//2+1])
    if i%2==0:
        if dpList[i-1]+1>dpList[i//2]+1:
            dpList.append(dpList[i//2]+1)
            if dpList[i-1]>dpList[i]+1:
                dpList[i-1] = dpList[i]+1
        else:
            dpList.append(dpList[i-1]+1)
    else:
        dpList.append(dpList[i-1]+1)
print(dpList[end])

