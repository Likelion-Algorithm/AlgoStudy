num = int(input())
sequence = list(map(int, input().split()))
dp = [0]
maxloc = 0
for i in range(len(sequence)):
    for j in range(len(dp)):
        if sequence[i]<=dp[j]:
            dp[j]=sequence[i]
            break
        if dp[j]==dp[-1]:
            dp.append(sequence[i])
print(len(dp)-1)

'''시간에서 별로 좋아보이지 않았는데 맞았다. 값이 주어지면
매번 모든 dp값과 비교하며 순열을 생성한다.'''