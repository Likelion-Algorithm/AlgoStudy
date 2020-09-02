def find(num,temp,m):
    if len(temp)==m:
        print(*temp)
        return
    for i in num:
        list1 = [str(j) for j in num if j != i]
        find(list1,temp+i,m)

import sys
n,m = map(int,sys.stdin.readline().split())
num = [str(i) for i in range(1,n+1)]
temp = ''
answer = []
find(num,temp,m)
