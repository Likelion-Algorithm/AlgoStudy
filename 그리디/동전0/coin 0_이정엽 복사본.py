import sys

repeat, num = map(int,sys.stdin.readline().split())

money = [int(sys.stdin.readline().strip()) for i in range(repeat)]
cnt = 0

while len(money) != 0:
    currency = money.pop()
    temp = num // currency
    if temp >0:
        cnt += temp
        num -= temp*currency
    if num == 0:
        break
print(cnt)




