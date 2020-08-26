import sys


def adjacent(k): #주변체크함수
    for i in range(k):
        if x[k] == x[i] or abs(x[k] - x[i]) == k- i: #수직 위 & 대각선 위
            return False
    return True

def nQueens(k):
    global cnt
    if k >= N: #k가 판의 끝까지 다다르면
        cnt += 1
    else:
        for c in range(N):
            x[k] = c
            if adjacent(k): #위에 겹치는 퀸이 없으면
                nQueens(k+1)
N = int(sys.stdin.readline())
x = [0] * N #해의 집합
cnt = 0

nQueens(0)
print(cnt)