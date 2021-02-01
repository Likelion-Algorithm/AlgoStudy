from collections import deque

M, N, H = map(int, input().split())
box = []
start = deque([])
for i in range(N*H):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j]==1:
            start.append(((i*M)+j,0))
    box.extend(temp)
if start:
    if len(start)==(M*N*H):
        print(0)
    else:
        while start:
            temp = start.popleft()
            loc = temp[0]
            day = temp[1]
            if (loc%M)+1<M and box[loc+1]==0:
                start.append((loc+1,day+1))
                box[loc+1]=1
            if (loc%M)-1>=0 and box[loc-1]==0:
                start.append((loc-1,day+1))
                box[loc-1]=1
            if (loc+M)%(M*N)>=M and box[loc+M]==0:
                start.append((loc+M,day+1))
                box[loc+M]=1
            if  loc%(M*N)>=M and box[loc-M]==0:
                start.append((loc-M,day+1))
                box[loc-M]=1
            if loc+(M*N)<(M*N*H) and box[loc+M*N]==0:
                start.append((loc+M*N,day+1))
                box[loc+M*N]=1
            if loc-(M*N)>=0 and box[loc-M*N]==0:
                start.append((loc-M*N,day+1))
                box[loc-M*N]=1
        if 0 in box:
            print(-1)
        else:
            print(day)
else:
    print(-1)

# 3->1차원 가상화
