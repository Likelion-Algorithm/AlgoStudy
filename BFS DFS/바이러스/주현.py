num = int(input())
pair = int(input())
linkedList = [[0 for col in range(num+1)] for row in range(num+1)]
stack = list()
virus = set()                               #바이러스가 걸린 컴퓨터의 set
for i in range(pair):                       #컴퓨터의 그래프 생성
    a,b = map(int, input().split())
    linkedList[a][b] = 1
    linkedList[b][a] = 1
stack.append(1)
while stack:                                #DFS탐색 
    loc = stack.pop()
    if loc not in virus:
        for i in range(num,-1,-1):
            if linkedList[loc][i]==1 :
                stack.append(i)
        virus.add(loc)                      #방문한 그래프에 대해 바이러스 판정
print(len(virus)-1)