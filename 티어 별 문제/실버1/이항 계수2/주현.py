a, b = map(int, input().split())
x, y = 1, 1
for i in range(b):
    x*= a-i
for i in range(1,b+1):
    y*=i
print(x//y%10007)

#combination