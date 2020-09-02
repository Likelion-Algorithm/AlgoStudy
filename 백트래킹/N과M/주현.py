N, M = map(int, input().split())
stack = list()
visited = [0]*M
for i in range(N,0,-1):
    stack.append([i,1])
while stack:
    temp = stack.pop()
    visited[temp[1]-1] = temp[0]
    if temp[1]!=M:
        for i in range(N,0,-1):
            if i not in visited[0:temp[1]]:
                stack.append([i,temp[1]+1])
    else:
        for i in visited:
            print(i, end = ' ')
        print()