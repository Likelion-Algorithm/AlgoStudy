N,K = input().split()
N = int(N)
K = int(K)
coin = list()
cost = 0
for i in range(N):
    coin.append(int(input()))
for i in range(N-1,-1,-1):
    cost += K//coin[i]
    K -= coin[i]*(K//coin[i])
    if(K==0):
        break
print(cost)