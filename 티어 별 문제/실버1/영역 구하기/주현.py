import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())
square = [[1 for x in range(N)] for y in range(M)]
for i in range(K):
    dx, dy, ux, uy = map(int, input().split())
    for x in range(dx,ux):
        for y in range(dy,uy):
            square[y][x] = 0
answer = []
controller = [(-1,0),(0,1),(1,0),(0,-1)]
def DFS(y,x):
    global square, temp
    for movex,movey in controller:
        if (x+movex>=0 and x+movex<N) and (y+movey>=0 and y+movey<M):
            if square[y+movey][x+movex]:
                square[y+movey][x+movex]=0
                temp+=1
                DFS(y+movey,x+movex)
for x in range(N):
    for y in range(M):
        if square[y][x]:
            temp = 1
            square[y][x]=0
            DFS(y,x)
            answer.append(temp)
answer.sort()
print(len(answer))
for i in answer:
    print(i, end=' ')