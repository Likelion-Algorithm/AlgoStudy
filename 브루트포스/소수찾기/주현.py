from itertools import permutations
def solution(numbers):
    n = len(numbers)
    answer = 0
    total = set()
    for i in range(1,n+1):
        temp = set(list(map(''.join, permutations(numbers,i))))
        temp = map(int,temp)
        total.update(temp)
    for i in total:
        if isPrime(i):
            answer+=1
    return answer
def isPrime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    else:
        return False