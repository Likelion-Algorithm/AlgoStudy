def isPrime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    else:
        return False
'''
def Prime(n):
    answer = 0
    for i in range(n+1 , n*2+1):
        if isPrime(i) == True:
            answer+=1
    return answer
'''
#원시적인 소수판별    
def Prime(n):
    primeList = []
    for i in range((2*n)+1):
        if isPrime(i) and i**2 <= 2*n:
            primeList.append(i)
        elif i**2 > 2*n:
            break
    answerList = []
    answer = 0
    for i in range(n+1,(n*2)+1):
        answerList.append(i)
    for i in answerList:
        for j in primeList:
            if i%j==0:
                answer+=1
                break
    return n-answer
#에라토스테네스의 체 알고리즘 적용 시 성공   

nList = []
n = int(input())
while n != 0:
    nList.append(n)
    n = int(input())
for i in nList:
    print(Prime(i))