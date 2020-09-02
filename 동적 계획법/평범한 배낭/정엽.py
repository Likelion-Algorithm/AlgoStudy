import sys
n,k = map(int,sys.stdin.readline().split())
answer = [0]*(k+1)
for j in range(n):
    w,v = map(int,sys.stdin.readline().split())
    for i in range(k,w-1,-1):
        answer[i] = max(answer[i],answer[i-w]+v)
print(max(answer))