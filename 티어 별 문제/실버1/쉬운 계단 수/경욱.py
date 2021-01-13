import sys
case = int(sys.stdin.readline())
dp = [0]+[1 for i in range(1, 10)]

for i in range(case-1):
    temp_list = [0 for i in range(10)]
    for j in range(len(dp)):
        if j == 0:
            if dp[j] != 0:
                temp_list[j+1] += dp[j]
        elif j == 9:
            temp_list[j-1] += dp[j]
        else:
            temp_list[j+1] += dp[j]
            temp_list[j-1] += dp[j]
    dp = temp_list
print(sum(dp) % 1000000000)
