import sys

N = int(sys.stdin.readline())
answer = [[0]*10 for _ in range(N)]

for i in range(N):
    for j in range(10):

        if i == 0:
            answer[i][j] = 1
        else:
            if j == 0:
                answer[i][j] = 1
            else:
                answer[i][j] = sum(answer[i-1][:j+1])
                # 이전것의 대각선끼리 더해도 됨

print(sum(answer[-1])%10007)
#통과