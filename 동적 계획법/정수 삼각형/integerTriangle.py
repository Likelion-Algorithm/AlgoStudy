import sys

n = int(input())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = []
for i in range(1, n + 1):
    result.append([0 for _ in range(i)])  # 결과 담을곳

for i in range(n):
    if i == 0:
        result[0][0] = triangle[0][0]
    else:
        for k in range(i + 1):
            if k == 0:  #왼쪽 끝
                result[i][k] = result[i - 1][k] + triangle[i][k]
            elif k == i:  # 오른쪽 끝
                result[i][k] = result[i - 1][k - 1] + triangle[i][k]
            else:
                if result[i - 1][k - 1] > result[i - 1][k]:  # 왼쪽대각선 위와 비교
                    result[i][k] = result[i - 1][k - 1] + triangle[i][k]
                else:  # 오른쪽대각선 위와 비교
                    result[i][k] = result[i - 1][k] + triangle[i][k]

print(max(result[n - 1]))  # 가장 아래층 비교
