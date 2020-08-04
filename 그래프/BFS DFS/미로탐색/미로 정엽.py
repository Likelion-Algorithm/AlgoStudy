import sys
import time
n,m = map(int,sys.stdin.readline().split())
maze = []
check = []
for i in range(n+2):
    maze.append([])
    maze[i].append(0)
    if (i == 0) or (i == n+1):
        for j in range(m):
            maze[i].append(0)
    else:
        check.append([])
        for j in sys.stdin.readline().strip():
            maze[i].append(int(j))
            check[-1].append(-1)
    maze[i].append(0)

queue = [(1,1)]
check[0][0] = 1

while queue:
    temp = []

    for i in queue:
        x = i[0]
        y = i[1]
        if maze[x-1][y] == 1:
            if check[x-2][y-1] == -1:
                check[x-2][y-1] = check[x-1][y-1] + 1
                temp.append((x-1,y))
            elif check[x-2][y-1] > check[x-1][y-1] + 1:
                check[x-2][y-1] = check[x-1][y-1]+1

        if maze[x+1][y] == 1:
            if check[x][y-1] == -1:
                check[x][y-1] = check[x-1][y-1] + 1
                temp.append((x+1,y))
            elif check[x][y-1] > check[x-1][y-1] + 1:
                check[x][y-1] = check[x-1][y-1]+1

        if maze[x][y-1] == 1:
            if check[x-1][y-2] == -1:
                check[x-1][y-2] = check[x-1][y-1] + 1
                temp.append((x,y-1))
            elif check[x-1][y-2] > check[x-1][y-1] + 1:
                check[x-1][y-2] = check[x-1][y-1]+1

        if maze[x][y+1] == 1:
            if check[x-1][y] == -1:
                check[x-1][y] = check[x-1][y-1] + 1
                temp.append((x,y+1))
            elif check[x-1][y] > check[x-1][y-1] + 1:
                check[x-1][y] = check[x-1][y-1]+1
    queue = temp[:]
print(check[-1][-1])

