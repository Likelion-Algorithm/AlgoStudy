import sys

N = int(sys.stdin.readline())
tmp = []
answer = [[0]*N for _ in range(N)]

for _ in range(N):
    tmp.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    if i == 0:
        answer[i][0] = tmp[i][0]
        answer[i][1] = tmp[i][1]
        answer[i][2] = tmp[i][2]
    else:
        answer[i][0] = tmp[i][0] + min(answer[i-1][1], answer[i-1][2])
        answer[i][1] = tmp[i][1] + min(answer[i-1][0], answer[i-1][2])
        answer[i][2] = tmp[i][2] + min(answer[i-1][0], answer[i-1][1])

# print(min(answer[-1]))
print(min(min(answer[N-1][0], answer[N-1][1]), answer[N-1][2]))
# 주석처리한 것이랑 위에거랑 다른게 뭔지 모르겠음.. 일단 통과
# 문제에서 조건이 이해가 안가서 찾아본 결과 결국 내 전꺼랑만 색이 같지 않으면 된다
#아직도 이해가 안되는 부분은 a!=b, b!=c이면 a!=c 아닌가..?ㅜㅜ
