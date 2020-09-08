import sys
from collections import deque
n = int(sys.stdin.readline().strip())
W = deque([int(sys.stdin.readline().strip()) for _ in range(n)])
for _ in range(3):
    W.appendleft(0)
DP = [0] * (n+3)

for i in range(3, n+3):
    DP[i] = max(DP[i-3]+W[i-1]+W[i], DP[i-2]+W[i], DP[i-1])
print(DP[-1])