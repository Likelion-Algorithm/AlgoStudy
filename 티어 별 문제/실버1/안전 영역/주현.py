N = int(input())
maxheight = 0
answer = 0
ground = []
for i in range(N):
    temp = list(map(int,input().split()))
    if max(temp)>maxheight:
        maxheight = max(temp)
    ground.append(temp)

def DFS(stack, n, visited):
    controller = [(-1,0),(0,1),(0,-1),(1,0)]
    while stack:
        loc = stack.pop()
        for x,y in controller:
            if (loc[0]+x>=0 and loc[0]+x<N) and (loc[1]+y>=0 and loc[1]+y<N) and not visited[((loc[0]+x)*N)+loc[1]+y]:
                if ground[loc[0]+x][loc[1]+y]>n:
                    stack.append((loc[0]+x,loc[1]+y))
                    visited[((loc[0]+x)*N)+loc[1]+y]=1
for height in range(maxheight):
    safty = 0
    visited = [0]*(N**2)
    for row in range(N):
        for col in range(N):
            if ground[row][col]>height and not visited[(row*N)+col]:
                stack = [(row,col)]
                visited[(row*N)+col]=1
                DFS(stack, height , visited)
                safty+=1
    if safty>answer:
        answer = safty

print(answer)