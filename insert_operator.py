import math
import sys

N = int(input())
nums = sys.stdin.readline().split()
num_operator = sys.stdin.readline().split()
for i in range(N):
    nums[i] = int(nums[i])

for j in range(4):
    num_operator[j] = int(num_operator[j])


maxmin = [-1000000000, 1000000000]
depth = 0
output = list()
output.append(nums[depth])


def dfs(output, depth):

    if depth == N-1:
        maxmin[0] = max(maxmin[0], output[-1])
        maxmin[1] = min(maxmin[1], output[-1])
        for k in range(len(output)-1):
            output.pop()
        return

    depth += 1
    next_num = nums[depth]

    if num_operator[0] > 0:
        num_operator[0] -= 1
        output.append(output[-1] + next_num)
        dfs(output, depth)
        num_operator[0] += 1

    if num_operator[1] > 0:
        num_operator[1] -= 1
        output.append(output[-1] - next_num)
        dfs(output, depth)
        num_operator[1] += 1

    if num_operator[2] > 0:
        num_operator[2] -= 1
        output.append(output[-1] * next_num)
        dfs(output, depth)
        num_operator[2] += 1

    if num_operator[3] > 0:
        num_operator[3] -= 1
        if (output[-1] < 0) or (next_num < 0):
            output.append(math.ceil((output[-1]) / next_num))
        else:
            output.append(output[-1] // next_num)
        dfs(output, depth)
        num_operator[3] += 1


dfs(output, depth)

print(maxmin[0], maxmin[1])