import sys
case = int(sys.stdin.readline())
for i in range(case):
    row = int(sys.stdin.readline())
    start = list(map(int, sys.stdin.readline().split()))
    end = list(map(int, sys.stdin.readline().split()))
    board = [[False for _ in range(row)] for _ in range(row)]
    stack = [start]

    def sol(row, start, end, board, stack):
        count = 0
        dx = [2, 2, -2, -2, -1, 1, -1, 1]
        dy = [-1, 1, 1, -1, 2, 2, -2, -2]
        if start == end:
            return 0
        while stack:
            # print(stack)
            temp = []
            for i in range(len(stack)):
                for j in range(8):
                    x = stack[i][0] + dx[j]
                    y = stack[i][1] + dy[j]
                    if [x, y] == end:
                        return count+1
                    elif 0 <= x < row and 0 <= y < row:
                        if board[x][y] == False:
                            board[x][y] = True
                            temp.append([x, y])
            stack = list(temp)
            count += 1
    a = sol(row, start, end, board, stack)
    print(a)
