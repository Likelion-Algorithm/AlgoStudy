def fibo(n):
    list1 = [0,1]
    if n<2:
        return list1[n]
    while(len(list1)!=(n+1)):
        list1.append(list1[-1]+list1[-2])
    return list1[-1]

import sys
print(fibo(int(sys.stdin.readline().strip())))