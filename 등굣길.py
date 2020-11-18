# 실패 

def dfs(i, j, m,n, matrix):
    global cnt
    cnt += 1
    matrix[i][j] = cnt

    if i ==m-1 and j == n-1:
        return cnt
    try:
        if matrix[i+1][j] != 'NA' and matrix[i+1][j] == 0:
            dfs(i+1,j, m,n,matrix)
        if matrix[i][j+1] != 'NA' and matrix[i][j+1] == 0:
            dfs(i, j+1, m,n,matrix)
    except IndexError:
        return

def solution(m, n, puddles):
    global cnt
    cnt = 0
    matrix = [[0]*m for _ in range(n)]
    for i in puddles: # 웅덩이 표시
        matrix[i[0]-1][i[1]-1] = 'NA'
    print(matrix)
    dfs(0,0,m,n, matrix )
    answer = 0
    print(matrix)
    return answer