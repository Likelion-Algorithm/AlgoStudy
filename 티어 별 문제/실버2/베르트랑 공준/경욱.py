import sys
vertex, edge = list(map(int,sys.stdin.readline().split()))
graph = dict()
visited = []
for i in range(edge):
  visited.append(False)

  begin,end = list(map(int,sys.stdin.readline().split()))
  try:
    graph[begin].append(end)
  except:
    graph[begin] = [end]
print(graph, visited)






