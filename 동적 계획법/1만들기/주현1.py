def makeone(n, a):
    
    if(n==1):
        return a
    elif(n%3==0 and n%2==0):
        defsum=[makeone(n/3, 0),makeone(n/2, 0),makeone(n-1,0)]
        if(min(defsum[0],defsum[1])==defsum[0]):
            return makeone(n/3,a+1)
        else:
            return makeone(n/2,a+1)
    elif(n%3==0):
        defsum=[makeone(n/3, 0),makeone(n-1,0)]
        return makeone(n/3,a+1) if (defsum[0]<defsum[1]) else makeone(n-1,a+1)
    elif(n%2==0):
        defsum=[makeone(n/2, 0),makeone(n-1,0)]
        return makeone(n/2,a+1) if (defsum[0]<defsum[1]) else makeone(n-1,a+1)
    else:
        return makeone(n-1,a+1)
n=int(input())
print(makeone(n,0))