def fibo(n):
    if(n==0):
        return 0 
    elif (n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input())
print(fibo(n))

'''문제만든놈이 0번째부터 시작해서 살짝 헷갈렸다. 뇌가 컴퓨터로
되어있는 놈인 것 같다.'''