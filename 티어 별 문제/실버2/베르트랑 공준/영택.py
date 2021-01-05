N = 123456
max_num = 0
isPrime = [False, False] + [True]*(2*N - 1)

def count_num(n):
    global max_num
    if max_num < n:
        for i in range(max_num*2 + 1, 2*n + 1): # max_num*2까지는 계산이 되었으므로
            if isPrime[i]:
                for j in range(2*i, 2*N + 1, i):
                    isPrime[j] = False
        max_num = n
        return isPrime[n+1:2*n + 1].count(True)
    else:
        return isPrime[n+1:2*n + 1].count(True)


while True:
    n = int(input())
    if n:
        print(count_num(n))
    else:
        break