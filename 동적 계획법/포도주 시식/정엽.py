import sys
n = int(sys.stdin.readline().strip())
a,b,c,d=0,0,0,0
for i in range(n):
    num = int(sys.stdin.readline().strip())
    a,b,c,d = c,max(d+num,a+num),max(a+num,b+num,d+num),a
print(max(a,b,c,d))