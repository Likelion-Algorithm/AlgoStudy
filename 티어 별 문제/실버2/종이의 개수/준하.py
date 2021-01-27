def answer(L, result):
    if len(L) == 1 or is_only(L):
        result[L[0][0]] += 1
        return

    rg = len(L) // 3

    nine_matrix = []

    for i in range(0, len(L), rg):
        for j in range(0, len(L), rg):
            temp = []
            rows = L[i:i + rg]
            for row in rows:
                temp.append(row[j:j + rg])
            nine_matrix.append(temp)

    for matrix in nine_matrix:
        answer(matrix, result)

from typing import List
def is_only(L: List) -> bool:
    num = L[0][0]
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] != num:
                return False
    return True


import sys
input = sys.stdin.readline
n = int(input())
G = []
for _ in range(n):
    G.append(list(map(int, input().split())))
result = [0, 0, 0]  # 0 1 -1
answer(G, result)
print(result[-1], result[0], result[1], sep='\n')
