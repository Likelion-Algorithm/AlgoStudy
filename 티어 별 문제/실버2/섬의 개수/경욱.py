import sys
result = []


def sol(board, check):
    count = 0
    x_check = [0, 0, 1, -1, -1, -1, 1, 1]
    y_check = [1, -1, 0, 0, -1, 1, -1, 1]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                board[i][j] = 0
                stack = [[i, j]]
                while stack:
                    temp = stack.pop()
                    x = temp[0]
                    y = temp[1]
                    for k in range(8):
                        new_x = x + x_check[k]
                        new_y = y + y_check[k]
                        if -1 < new_x < h and -1 < new_y < w:
                            temp_check = board[new_x][new_y]
                            if temp_check == 1:
                                stack.append([new_x, new_y])
                                board[new_x][new_y] = 0
                count += 1
                # board[i-x[k]][j-y[k]]

    return count


while True:
    board = []
    w, h = list(map(int, sys.stdin.readline().split()))
    if w == 0 and h == 0:
        break
    for i in range(h):
        temp = list(map(int, sys.stdin.readline().split()))
        board.append(temp)
    check = list(board)
    a = sol(board, check)
    result.append(a)
for i in result:
  print(i)
