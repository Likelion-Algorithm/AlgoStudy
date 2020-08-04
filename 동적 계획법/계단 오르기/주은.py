NUM_STAIRS = int(input())
stair = []
P = []
idx = []

for i in range(NUM_STAIRS):
    stair.append(int(input()))

stair.reverse()

P.append(stair[0])
idx.append(0)
P.append(P[0]+stair[1])
idx.append(1)

for i in range(2, NUM_STAIRS):
    if ( ((i - 1) in idx) & ((i - 2) in idx) ):
        if(P[i-1] <= P[i-2] + stair[i]):
            idx.remove(i-1)
            idx.append(i)
            P.append(P[i-2] + stair[i])
        else:
            P.append(P[i-1])

    else:
        idx.append(i)
        P.append(P[i-1] + stair[i])

print(P)
print(idx)
print(P[NUM_STAIRS-1])
