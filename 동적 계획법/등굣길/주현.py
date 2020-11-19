def solution(m, n, puddles):
    answer = 0
    dp = [[0 for col in range(m+1)] for row in range(n+1)]
    dp[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if not(i==1 and j==1) and [j,i] not in puddles:
                a = dp[i-1][j] 
                b = dp[i][j-1] 
                dp[i][j] = a + b

    answer=dp[-1][-1]
    return answer%1000000007
print(solution(4,3,[[2,2]]))