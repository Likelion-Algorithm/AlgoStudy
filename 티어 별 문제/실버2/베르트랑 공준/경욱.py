import sys


def sol(n):
    if n == 1:
        return 1
    check = [True] * (2 * n + 1)
    m = int((2 * n) ** 0.5)
    for i in range(2, m+1):
        if check[i] == True:
            for j in range(i+i, 2*n, i):
                check[j] = False
    # print(check, check[n+1:2*n].count(True))
    return check[n+1:2*n].count(True)


while 1:
    a = int(input())
    if a == 0:
        break
    else:
        print(sol(a))

# # check = []
# a = 1
# while a != 0:
#     a = int(sys.stdin.readline())
#     if a == 0:
#         break
#     if a == 1:
#         print(1)
#         continue
#     count = 0
#     for i in range(a+1, 2*a):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#             elif j == i-1 and i % j != 0:
#                 # print(i)
#                 count += 1
#     print(count)
#     # check.append(a)
# # check.sort(reverse=True)
# # for i in range(len(check)-2, -1, -1):
