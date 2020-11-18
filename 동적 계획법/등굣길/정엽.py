def solution(m,n,puddles):
    path = [[0]*(m+1)]
    path += [[0]+([float('inf')]*m) for i in range(n)]
    path[1][1] = 1
    for y,x in puddles:
        path[x][y] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if path[i][j] == 0 or (i == 1 and j == 1):
                continue
            else:
                path[i][j] = path[i-1][j] + path[i][j-1]
    return [path[n][m] % 1000000007,0][path[n][m] == float('inf')]