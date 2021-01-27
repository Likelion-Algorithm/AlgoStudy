import sys
row = int(sys.stdin.readline())


def sol(start, end, temp):
    if start == end:
        for i in range(len(temp)):
            print("".join(temp[i]))
        return temp
    temp_board = list(temp) * 3

    for i in range(0, len(temp_board)):
        if i <= start-1:
            temp_board[i] = temp_board[i] * 3
        elif start-1 < i <= start*2-1:
            temp_board[i] = temp_board[i] + [" "] * len(temp) + temp_board[i]
        else:
            temp_board[i] = temp_board[i] * 3
    return sol(start * 3, end, temp_board)


sol(1, row, [["*"]])
