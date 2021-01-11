from collections import deque

w, h =map(int,input().split())
answer = []
controll = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
while w!=0 and h !=0:
    graph = []
    queue = deque([])
    for i in range(h):
        graph.append(list(map(int,input().split())))
    land = 0
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1:
                queue.append([x,y])
                graph[x][y] = 0
                land+=1
                while queue:
                    locX , locY = queue.popleft()
                    graph[locX][locY] = 0
                    for moveX, moveY in controll:
                        if locX+moveX<h and locY+moveY<w and locX+moveX>=0 and locY+moveY>=0:
                            if graph[locX+moveX][locY+moveY]==1:
                                queue.append([locX+moveX,locY+moveY])
                                graph[locX+moveX][locY+moveY]=0
    answer.append(land)
    w, h =map(int,input().split())
for i in answer:
    print(i)

#9방향 컨트롤을 리스트로 풀이
#방문체크는 큐에 append시 해야 불필요한 append를 방지할 수 있다.(pop과 방문체크 시 매우 비효율적)