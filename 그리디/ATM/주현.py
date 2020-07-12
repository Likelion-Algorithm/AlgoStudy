N = int(input())
plist = list(map(int,input().split()))
timesum = 0
plist.sort()
for i in range(N+1):
    timesum += sum(plist[0:i])
print(timesum)

'''정렬 후 더해가면 그리디 알고리즘이 수행된다. 정렬이 될 수록 
   큰 수의 사용이 최소화 되기 때문이다.'''
