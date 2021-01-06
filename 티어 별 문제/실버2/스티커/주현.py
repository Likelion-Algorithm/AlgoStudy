T = int(input())
answer = []

def dp(sticker, n):
    value = [0]*((n+2)*2)
    for i in range(2,n+2):
        value[i] = max(value[i+n]+sticker[i-2],value[i+n+1]+sticker[i-2],value[i-2]+sticker[i-2] )
        value[i+n+2] = max(value[i-1]+sticker[i-2+n],value[i-2]+sticker[i-2+n],value[i+n]+sticker[i-2+n])
    return max(value)
for i in range(T):
    n = int(input())
    sticker = list(map(int,input().split()))
    sticker.extend(list(map(int,input().split())))
    answer.append(dp(sticker, n))

for i in answer:
    print(i)