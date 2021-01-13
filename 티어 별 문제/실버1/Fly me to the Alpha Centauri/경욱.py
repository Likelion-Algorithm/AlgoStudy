import sys
case = int(sys.stdin.readline())
for i in range(case):
    start, end = list(map(int, sys.stdin.readline().split()))
    length = end - start
    if length <= 3:
        print(length)
    else:
        a = int(length ** 0.5)
        if length == a ** 2:
            print(2*a - 1)
        elif a**2 < length <= a**2 + a:
            print(2 * a)
        else:
            print(2*a+1)


# 메모리 초과 풀이
# import sys
# case = int(sys.stdin.readline())
# for i in range(case):
#     start, end = list(map(int, sys.stdin.readline().split()))
#     length = end-start - 2
#     check = [[[1, 1]]] + [[] for _ in range(length)] + [[]]
#     for i in range(len(check)-1):
#         print(check)
#         for j in range(len(check[i])):
#             if i == len(check)-2 and check[i][j][0] < 3:
#                 print(check[i][j][1] + 1)
#                 break
#             if check[i][j][0] - 1 > 0 and i + check[i][j][0]-1 < len(check):
#                 if [check[i][j][0]-1, check[i][j][1]+1] not in check[i + check[i][j][0] - 1]:
#                     check[i + check[i][j][0] -
#                           1].append([check[i][j][0]-1, check[i][j][1]+1])
#             if i + check[i][j][0] + 1 < len(check):
#                 if [check[i][j][0]+1, check[i][j][1]+1] not in check[i + check[i][j][0] + 1]:
#                     check[i + check[i][j][0] +
#                           1].append([check[i][j][0]+1, check[i][j][1]+1])
#             if i + check[i][j][0] < len(check):
#                 if [check[i][j][0], check[i][j][1]+1] not in check[i + check[i][j][0]]:
#                     check[i+check[i][j][0]
#                           ].append([check[i][j][0], check[i][j][1]+1])
