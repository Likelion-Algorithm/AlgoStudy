from itertools import permutations

N = int(input())
array = list(map(int,input().split()))

def cuscal(A,n):
    total = 0
    for i in range(0,n-1):
        total += abs(A[i]-A[i+1])
    return total
answer = permutations(array,N)
temp = 0
for i in answer:
    if temp < cuscal(i,N):
        temp = cuscal(i,N)
print(temp)