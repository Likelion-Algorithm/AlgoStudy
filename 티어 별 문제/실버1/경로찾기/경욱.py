import sys
row = int(sys.stdin.readline())
board = []
for i in range(row):
    board.append(list(map(int, sys.stdin.readline().split())))


for i in range(row):
    stack = []
    check = [False for _ in range(row)]
    for j in range(row):
        if board[i][j] == 1 and check[j] == False:
            check[j] = True
            stack.append(j)
            while stack:
                temp = stack.pop()
                for k in range(row):
                    if board[temp][k] == 1 and check[k] == False:
                        board[i][k] = 1
                        check[k] = True
                        stack.append(k)
for i in board:
    print(*i)
 
# stack = []
# for i in range(row):
#     for j in range(row):
#         if board[i][j] == 1:
#             stack.append(j)
#             count = 0
#             while stack:
#                 print(board, stack)
#                 count += 1
#                 if count == 1:
#                     break
#                 temp = stack.pop()
#                 for k in range(len(board[temp])):
#                     if board[temp][k] == 1:
#                         board[i][k] = 1
#                         if k != i:
#                             stack.append(k)


# import timeit

# start_time = timeit.default_timer() # 시작 시간 체크

# sum = 0

# for i in range(10000000):
#     sum += i

# terminate_time = timeit.default_timer() # 종료 시간 체크

# print("%f초 걸렸습니다." % (terminate_time - start_time))
