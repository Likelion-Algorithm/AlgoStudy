num, total = map(int, input().split())

coins = [int(input()) for _ in range(num)]

cnt = 0

for _ in range(num):
    a = coins.pop()
    b = total//a
    if b != 0:
        total -= a*b
        cnt += b

print(cnt)