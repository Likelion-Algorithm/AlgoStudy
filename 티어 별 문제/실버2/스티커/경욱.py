import sys


def sol():
    col = int(sys.stdin.readline())
    # board = [
    #     [0, 50, 10, 100, 20, 40],
    #     [0, 30, 50, 70, 10, 60]
    # ]
    board = []
    for _ in range(2):
        board.append([0] + list(map(int, sys.stdin.readline().split())))
    for i in range(2, len(board[0])):
        # board[0][i] = max(board[0][i-2]+board[1][i-1], board[1][i-2])
        # board[1][i] = max(board[1][i-1]+board[0][i-1], board[])
        board[0][i] += max(board[1][i-1], board[1][i-2])
        board[1][i] += max(board[0][i-1], board[0][i-2])
    print(max(board[0][-1], board[1][-1]))
    return


case = int(sys.stdin.readline())
for i in range(case):
    sol()
