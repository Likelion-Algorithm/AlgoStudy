N = int(input())
jump = []
dp = [0]*(N*N)
for i in range(N):
    jump.extend(list(map(int, input().split())))
dp[0]=1
for i in range((N*N)):
    v = jump[i]
    if dp[i] and i!=(N*N)-1:
        if i%N+v<N:
            dp[i+v]+=dp[i]
        if i//N+v<N:
            dp[i+(v*N)]+=dp[i]
        
print(dp[-1])

# 2차원 배열 가상화

'''
def cusSearch(x,y):
    global answer
    value = jump[x][y]
    if x==N-1 and y==N-1:
        answer+=1
        return
    if x+value<N:
        cusSearch(x+value,y)
    if y+value<N:
        cusSearch(x,y+value)
cusSearch(0,0)
print(answer)
'''