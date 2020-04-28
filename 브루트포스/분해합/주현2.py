n = int(input(""))
def hap(n):
    for i in range(n-((jisoo(n)+1)*9),n+1):
        for j in range(jisoo(n)-1,jisoo(n)+1):
            if(10**j<=i<10**(j+1)):
                a=bunhae(i)
                if(a==n):
                    print(i)
                    return 0
        
    print(0)
    return 0

def jisoo(n):
    a=0
    while n>10:
        n=n/10
        a+=1
    return a

def bunhae(n):
    a=0
    b=str(n)
    for i in b:
        a+=int(i)
    return a+n
        
hap(n) 