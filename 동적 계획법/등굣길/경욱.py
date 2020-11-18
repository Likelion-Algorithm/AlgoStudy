def solution(m, n, puddles):
    answer = 0
    board = []
    for i in range(n+2):
        if i == 0 or i == n+1:
            board.append([float('inf') for _ in range(m+2)])
        else:
            board.append([float('inf')] + [0 for _ in range(m)] + [float('inf')])
    for i in range(len(puddles)):
        board[puddles[i][1]][puddles[i][0]] = float('inf')
    board[1][1]=1
    need_visit = [[1,1]]
    while need_visit:
        temp_list = list()
        for i in need_visit:
            # print(i)
            x = i[0]
            y = i[1]
            if i == [m,n] :
                answer +=1
            if board[y][x+1] !=float('inf'):
                board[y][x+1] +=board[y][x]
                temp_list.append((x+1,y))
            if board[y+1][x] != float('inf'):
                board[y+1][x] += board[y][x]
                temp_list.append((x,y+1))
        need_visit = set(temp_list)
    return board[n][m] % 1000000007
a = solution(4,3,[[2,2]])
print(a)
# def solution(m, n, puddles):
#     global answer
#     answer = 10000000007
#     board = []
#     final = []
#     for i in range(n+2):
#         if i == 0 or i == n+1:
#             board.append([True for _ in range(m+2)])
#         else:
#             board.append([True] + [False for _ in range(m)] + [True])
#     # board = [[False for _ in range(m)] for _ in range(n)]
#     for i in range(len(puddles)):
#         board[puddles[i][0]][puddles[i][1]] = True
#     def DFS(end, board, need_visit, depth):
#         global answer
#         if need_visit == end:
#             if answer > depth:
#                 answer = depth
#                 final.clear()
#                 final.append(1)
#                 return
#             elif answer == depth:
#                 final.append(1)
#                 return
#             elif answer < depth:
#                 return
            
#         x = need_visit[0]
#         y = need_visit[1]   
#         if board[y][x+1] == False:
#             board[y][x+1] = True
#             DFS(end, board, [x+1,y], depth+1)
#             board[y][x+1] = False
#         if board[y+1][x] == False:
#             board[y+1][x] = True
#             DFS(end, board, [x,y+1], depth+1)
#             board[y+1][x] = False
        
#     print(board)
#     DFS([m,n], board, [1,1], 0)
    
#     return len(final)
# a = solution(4,3,[[2,2]])
# print(a)