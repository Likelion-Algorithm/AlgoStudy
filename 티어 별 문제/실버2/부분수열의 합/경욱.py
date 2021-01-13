import sys
from itertools import combinations
count = 0
num, sum_num = list(map(int, sys.stdin.readline().split()))
board = list(map(int, sys.stdin.readline().split()))
for i in range(len(board)):
    com_list = list(combinations(board, i+1))
    for j in com_list:
        if sum(j) == sum_num:
            count += 1
print(count)
