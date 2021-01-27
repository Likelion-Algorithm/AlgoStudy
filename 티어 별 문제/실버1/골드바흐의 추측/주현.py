N = int(input())
answer = []
for i in range(N):
    answer.append(int(input()))

def gold(n):
    for i in range(n//2,1,-1):
        if isPrime(i):
            if isPrime(n-i):
                return [i,n-i]

def isPrime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    else:
        return False
for i in answer:
    for primes in gold(i):
        print(primes, end=' ')
    print()