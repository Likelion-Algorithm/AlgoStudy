# psuedo code
# k는 행, N은 판 넓이
# def nQeens(k): # x[k]를 결정(열번호)(x[0]~x[n-1])
#     if k >= N: #체스판의 끝까지 결정되었다면
#         return
#     for c in range(N):
#         if queen can place at (k, c): # 충돌 판별함수 호출
#             x[k] = c
#             nQeens(k+1)
import sys
from collections import deque
N = int(sys.stdin.readline())
# x = defaultdict(int)# 퀸의 위치를 나타내는 딕셔너리
x = deque()
cnt = 0
def nQueens(k):
    global cnt
    if k >= N :
        cnt += 1
        return cnt
    for c in range(N):
        if x:
            print(x)
            row, col = x.popleft()
            if col == c : #같은 라인에 퀸 있을경우
                if c == N-1:
                    return
                continue
            elif (k + c ) == (row+ col) or (k-c) == (row- col): #오른쪽 대각선 & 왼쪽 대각선 점검
                if c == N-1:
                    return
                continue
            x.append((k,c))
            nQueens(k+1)
        else:
            x.append((k,c))
            nQueens(k+1)
nQueens(0)
print(cnt)