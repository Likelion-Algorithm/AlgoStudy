def dfs(dfsStack,complex,house):
    temp = 0
    while dfsStack:
        loc = dfsStack.pop()
        if loc not in complex:                      #상하좌우에 대해 DFS를 실시한다.
            if house[loc[0]-1][loc[1]]==1:
                dfsStack.append([loc[0]-1,loc[1]])
            if house[loc[0]][loc[1]-1]==1:
                dfsStack.append([loc[0],loc[1]-1])
            if  house[loc[0]][loc[1]+1]==1:
                dfsStack.append([loc[0],loc[1]+1])
            if  house[loc[0]+1][loc[1]]==1:
                dfsStack.append([loc[0]+1,loc[1]])
            complex.append(loc)
            temp+=1                                 #방문기록을 temp에 남긴다.
    return temp
size = int(input())
house = []                                          #input그래프 
complex = []                                        #아파트 단지로 지정된 그래프 목록
dfsStack = []                                       #DFS실시를 위한 스택
sizeList = []                                       #단지 크기를 저장하는 리스트

for i in range(size+2):                             #상하좌우를 탐색하므로 런타임에러를 막기위해 화려한0으로 감싼다.
    if i == 0:
        house.append([])
        for j in range(size+2):
            house[i].append(0)
    elif i == size+1:
        house.append([])
        for j in range(size+2):
            house[i].append(0)
    else:
        house.append(list(map(int, input())))
        house[i].insert(0,0)
        house[i].append(0)

for i in range(1,size+1):
    for j in range(1,size+1):
        if house[i][j]==1 and [i,j] not in complex:
            dfsStack.append([i,j])
            sizeList.append(dfs(dfsStack,complex,house))
        
sizeList.sort()
print(len(sizeList))
for i in sizeList:
    print(i)

