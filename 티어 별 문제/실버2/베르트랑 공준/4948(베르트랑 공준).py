import sys

def FindPrimeNum(num):
    if num <2:
        return True
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

def solution(n):
    cnt = 0

    for i in range(n+1, (2*n)+1):
        if FindPrimeNum(i):
           cnt += 1
    answer.append(cnt)

answer = []
while True:
    target = int(sys.stdin.readline())
    
    if target == 0:
        for i in answer:
            print(i)
        break
    else:
        solution(target)

#답은 맞는데 백준 시간초과ㅠ
