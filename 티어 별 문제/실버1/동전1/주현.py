n, k = map(int,input().split())

DP = [0]*(k+1)
DP[0] =1
values = [0]
for i in range(n):
    values.append(int(input()))

for i in range(1,n+1):
    for j in range(1, k+1):
        if j>=values[i]:
            DP[j] +=  DP[j-values[i]]
        
print(DP[-1])

#이거 한 적 있는데요...?