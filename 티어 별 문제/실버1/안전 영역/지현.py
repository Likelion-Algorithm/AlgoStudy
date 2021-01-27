import sys

N = int(sys.stdin.readline())
lst = []
nums = set()

for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    lst.append(a)
    nums.update(a)
nums = sorted(list(nums))
nums.insert(0,0)
rainrate = [0]*len(nums)

for k in range(len(nums)):
    if nums[k] == 0:
        rainrate[k] = 1

    else:
        cnt = 0
        checker = [[0]*N for _ in range(N)]
        stack = []

        for i in range(N):
            for j in range(N):
                if lst[i][j] > nums[k] and checker[i][j] == 0:
                    stack.append((i, j))
                    checker[i][j] = 1

                    while stack:
                        x_, y_ = stack.pop()

                        x = [1, -1, 0, 0]
                        y = [0, 0, 1, -1]

                        for l in range(4):
                            xd = x_+x[l]
                            yd = y_+y[l]

                            if 0 <= xd <= (N-1) and 0 <= yd <= (N-1) and lst[xd][yd] > nums[k] and checker[xd][yd] == 0:
                                checker[xd][yd] = 1
                                stack.append((xd, yd))
                    cnt +=  1
        rainrate[k] = cnt

print(max(rainrate))
# 통과
# 재귀로 시도했다가 재귀횟수제한에 걸려 dfs로 변경
# 비가 오지 않은 경우도 포함