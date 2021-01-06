n = int(input())
RGB = []
DP = [float('inf')]*(n*3)
for i in range(n):
    RGB.extend(list(map(int,input().split())))
for i in range(n*3):
    if i < 3 :
        DP[i] = RGB[i]
    else:
        if i%3 == 0 :
            DP[i] = RGB[i]+min(DP[i-1],DP[i-2])
        elif i%3 ==1:
            DP[i] = RGB[i]+min(DP[i-2],DP[i-4])
        else:
            DP[i] = RGB[i]+min(DP[i-4],DP[i-5])
print(min(DP[-3:]))