import sys
from itertools import combinations
board = []
while True:
    temp = list(map(int, sys.stdin.readline().split()))
    if temp[0] == 0:
        break
    board.append(temp[1:])
for i in board:
    a = list(combinations(i, 6))
    for j in a:
        print(*j)
    print()
