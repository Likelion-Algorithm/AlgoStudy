import sys

T = int(sys.stdin.readline())
answer = []

def Solution():
    n = int(sys.stdin.readline())
    stickers = []
    checker = [[0]*(n) for _ in range(2)]

    for _ in range(2):
        sticker = list(map(int, sys.stdin.readline().split()))
        stickers.append(sticker)
    
    for i in range(n):
        for j in range(2):
            if i == 0:
                checker[j][i] = stickers[j][i]
            elif i == 1:
                if j == 0:
                    checker[j][i] = checker[j+1][i-1] + stickers[j][i]
                else:
                    checker[j][i] = checker[j-1][i-1] + stickers[j][i]
            else:
                if j == 0:
                    checker[j][i] = max(stickers[j][i] + checker[j+1][i-1], stickers[j][i] + checker[j+1][i-2])
                else:
                    checker[j][i] = max(stickers[j][i]+ checker[j-1][i-1], stickers[j][i] + checker[j-1][i-2])
    
    a = checker[0].pop()
    b = checker[1].pop()
    answer.append(max(a,b))
 
for _ in range(T):
    Solution()

for i in answer:
    print(i)

#통과