import sys
num = int(sys.stdin.readline())
board = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
temp = list(board)
for _ in range(num-1):
    for i in range(len(board)-1):
        for j in range(i+1, len(board)):
            temp[j] += board[i]
    board = list(temp)
print(sum(board) % 10007)
