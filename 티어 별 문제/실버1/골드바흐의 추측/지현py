import sys 

T = int(sys.stdin.readline())
answers = []


def primenum_list(n):
    checker = [True]*n
    m = int(n**0.5)
    
    for i in range(2, m+1):
        if checker[i] == True:
            for j in range(i+i, n, i):
                checker[j] = False
    return [i for i in range(2, n) if checker[i] == True]

def partition_(primenum, n):
    tmp = []

    for i in range(len(primenum)-1, -1,-1):
        target = n-primenum[i]

        for j in range(i, len(primenum)):
            if primenum[j] == target:
                tmp.append((primenum[i], primenum[j], primenum[j]-primenum[i]))

    tmp.sort(key = lambda x:x[2])
    answers.append(tmp[0])


for _ in range(T):
    n = int(sys.stdin.readline())
    primenum = primenum_list(n)
    partition_(primenum, n)

for answer in answers:
    print(answer[0], answer[1])


#pypy에서 통과
#에라토스테네스의 체 원리 이해 잘 안감ㅠㅠㅠ오ㅐ 0.5를 제곱해주는걸까!!!!!!