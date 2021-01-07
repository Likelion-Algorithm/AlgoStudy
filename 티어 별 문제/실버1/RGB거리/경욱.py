import sys
num_input = int(sys.stdin.readline())
check = [list(map(int, sys.stdin.readline().split())) for i in range(num_input)]

for i in range(1,len(check)):
  for j in range(len(check[i])):
    check[i][j] += min(check[i-1][:j]+check[i-1][j+1:])
print(min(check[-1]))