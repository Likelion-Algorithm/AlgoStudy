def fivo(n):
    if n<=1:    #n이 1 이하일때는 n을 반환(n=1이면 1반환, 0이면 0반환)
        return n
    return(fivo(n-1)+fivo(n-2))

num=int(input())
print(fivo(num))