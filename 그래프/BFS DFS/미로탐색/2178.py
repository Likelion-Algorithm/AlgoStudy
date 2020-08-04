import sys

n ,m = map(int, sys.stdin.readline().split())
graph = [] # 입력값을 받는 리스트
graph_count = [] #(1,1)에서 출발하여 (n,m)에 도착할 때까지 이동 횟수 기록용

for _ in range(n):
    graph.append(list(str(sys.stdin.readline().rstrip())))

graph.insert(0, [str(0)]*(m+2))
graph.insert(len(graph), [str(0)]*(m+2)) 

for i in range(1, n+1):
    graph[i].insert(0, str(0))
    graph[i].insert(len(graph[i]), str(0)) #인덱스 에러가 발생하지 않도록 겉부분을 0으로 채워줌 -> (1,1) 인덱스부터 출발

for _ in range(n+2):
    graph_count.append([0] * (m+2)) # 이동 횟수 기록용 리스트도 같은 수만큼 전체 0으로 채워줌


def DFS(graph, graph_count, n, m):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1] # 상하좌우 탐색

    queue = [[1,1]] #DFS 방식이므로 큐 활용, (1,1)부터 시작이므로 미리 큐 안에 넣어줌
    graph_count[1][1] = 1 # 이동 횟수 기록용 리스트의 (1,1) 인덱스 값을 1로 변경(시작 위치를 이동 횟수에 포함하므로)

   
    while queue: # 큐가 빌때까지
        num1 = queue[0][0] 
        num2 = queue[0][1] #큐의 첫 번째 값들의 x좌표, y좌표를 num1, num2 변수에 저장

        queue.pop(0) 

        for k in range(4): 
            x = dx[k] + num1 
            y = dy[k] + num2 # num1,num2(기준좌표)의 상하좌우를 탐색하면서
            
            if graph[x][y] == str(1) and graph_count[x][y] == 0 and [x,y] not in queue: # 값이 1이며, 방문하지 않았으며, 좌표값의 리스트가 큐 내에도 존재하지 않을 때
                
                graph_count[x][y] = graph_count[num1][num2] + 1 #이동횟수 리스트의 값(0)을 기준좌표 이동횟수 리스트의 값에 1을 더해준 값으로 만들어줌 -> 이동할때마다 수가 점차 증가
                queue.append([x,y]) #큐 내에 넣어줌
    
    return graph_count[n][m] #while문이 끝난 후 (n,m) 좌표의 이동횟수 리스트 값을 리턴
            
        
print(DFS(graph,graph_count, n,m))