import sys


def sol(height, board, row):
    temp_check = [[False for _ in range(row)] for _ in range(row)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    count = 0
    need_visit = []
    for j in range(row):
        for k in range(row):
            if height < board[j][k] and temp_check[j][k] == False:
                need_visit.append([j, k])
                temp_check[j][k] = True
                while need_visit:
                    temp = need_visit.pop()
                    for z in range(len(dx)):
                        x = temp[0] + dx[z]
                        y = temp[1] + dy[z]
                        if 0 <= x < len(temp_check) and 0 <= y < len(temp_check):
                            if temp_check[x][y] == False and board[x][y] > height:
                                need_visit.append([x, y])
                                temp_check[x][y] = True
                count += 1
    return count


row = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

result = 1
for height in range(1, 101):
    temp = sol(height, board, row)
    if temp > result:
        result = temp
print(result)
