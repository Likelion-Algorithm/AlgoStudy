def find(n,k):
    if n>= k:
        return n-k
    elif k == 1:
        return 1
    elif k%2:
        return min(find(n,k+1),find(n,k-1))+1
    else:
        return min(k-n,1+find(n,k//2))

import sys
n,k = map(int,sys.stdin.readline().split())
print(find(n,k))
