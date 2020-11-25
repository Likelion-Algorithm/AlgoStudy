def solution(n, results):
    answer = 0
    graph = list()
    for i in range(n):
        graph.append([float('inf') for _ in range(n)])
    for i in results:
        graph[i[0]-1][i[1]-1] = 1
        graph[i[1]-1][i[0]-1] = 0

    for i in range(n):
      for j in range(n):
        for k in range(n):
          if graph[j][k] == float('inf') and graph[j][i]+ graph[i][k] == 2:
            graph[j][k] = 1
            graph[k][j] = 0
    for i in range(n):
      if graph[i].count(float('inf')) == 1:
        answer +=1
    return answer