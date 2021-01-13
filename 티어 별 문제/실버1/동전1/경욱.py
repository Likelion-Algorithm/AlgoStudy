import sys
num, amount = list(map(int, sys.stdin.readline().split()))
coins = []
for i in range(num):
    coins.append(int(sys.stdin.readline()))
check = [1] + [0 for _ in range(amount)]
for i in range(len(coins)):
    temp = list(check)
    for j in range(len(check)):
        if j < coins[i]:
            temp[j] = check[j]
        else:
            temp[j] = check[j] + temp[j-coins[i]]
    check = list(temp)

print(check[-1])
