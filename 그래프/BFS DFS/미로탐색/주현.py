import sys
N ,M = map(int,sys.stdin.readline().strip().split())
miroList = list()
visitList = list()
queueList = list()
for i in range(N+2):                    #그래프 생성
    if i == 0:
        miroList.append([])
        for j in range(M+2):
            miroList[i].append(0)
    elif i == N+1:
        miroList.append([])
        for j in range(M+2):
            miroList[i].append(0)
    else:
        miroList.append([0])
        miroList[i].extend(list(map(int, sys.stdin.readline().strip())))
        miroList[i].append(0)
queueList.append([1,1])

while queueList:                        #BFS실시하며 탐색경로 기록
    loc = queueList.pop(0)
    temp = len(queueList)
    if loc not in visitList:
        visitList.append([loc[0],loc[1]])
        if miroList[loc[0]][loc[1]+1]==1 and [loc[0],loc[1]+1] :
            queueList.append([loc[0],loc[1]+1])
        if miroList[loc[0]-1][loc[1]]==1 and [loc[0]-1,loc[1]] :
            queueList.append([loc[0]-1,loc[1]])
        if miroList[loc[0]+1][loc[1]]==1 and [loc[0]+1,loc[1]] :
            queueList.append([loc[0]+1,loc[1]])
        if miroList[loc[0]][loc[1]-1]==1 and [loc[0],loc[1]-1] :
            queueList.append([loc[0],loc[1]-1])
        
length = 1
a = visitList.index([N,M])
temp = [N,M]
for i in range(a,0,-1):                 #미로 출구에서 반대로 선을 그려 찾는다.
    if [temp[0],temp[1]+1] == visitList[i-1]:
        temp = visitList[i-1]
        length+=1
    elif [temp[0]-1,temp[1]] == visitList[i-1]:
        temp = visitList[i-1]
        length+=1
    elif [temp[0]+1,temp[1]] == visitList[i-1]:
        temp = visitList[i-1]
        length+=1
    elif [temp[0],temp[1]-1] == visitList[i-1]:
        temp = visitList[i-1]
        length+=1
print(length)

