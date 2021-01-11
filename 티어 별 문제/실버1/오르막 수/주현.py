N = int(input())
DP = [1,1,1,1,1,1,1,1,1,1]
for i in range(1,N+1):
    for j in range(10):
        DP[j] =  sum(DP[j:])
print(DP[0]%10007)

#   1   1   1   1   1   1   1   1   1   1   
#   10  9   8   7   6   5   4   3   2   1
#   55  45  36 ~~~~~ 