row, column = map(int, input().split())
maze = []
visited = []
queue = []
graph = {}
child = 0

for i in range (row):
    maze.append(list(input()))

queue.append((0, 0))
visited.append((0, 0))

while( len(queue) != 0 ):
    x, y = queue[0]
    key = (x, y)

    # 오른쪽 (우선순위1)
    if ( y+1 < column ):
        if ( (maze[x][y+1] == '1') and ((x, y+1) not in visited) ):
            child += 1
            print('>')
            queue.append((x, y+1))
            visited.append((x, y+1))
            if((x == row-1) and (y+1 == column-1) ):
                graph[key] = (x, y+1)
                break

    # 아래 (우선순위2)
    if ( x+1 < row ):
        if ( maze[x+1][y] == '1' and ((x+1, y) not in visited) ):
            child += 1
            print('v')
            queue.append((x+1, y))
            visited.append((x+1, y))
            if((x+1 == row-1) and (y == column-1)):
                graph[key] = (x+1, y)
                break

    # 위
    if ( x-1 >= 0 ):
        if ( maze[x-1][y] == '1' and ((x-1, y) not in visited) ):
            child += 1
            print('^')
            queue.append((x-1, y))
            visited.append((x-1, y))
            if((x-1 == row-1) and (y == column-1)):
                graph[key] = (x-1, y)
                break
    
    # 왼쪽
    if ( y-1 >= 0 ):
        if ( maze[x][y-1] == '1' and ((x, y-1) not in visited) ):
            child += 1
            print('<')
            queue.append((x, y-1))
            visited.append((x, y-1))
            if((x == row-1) and (y-1 == column-1) ):
                graph[key] = (x, y-1)
                break
    
    print(queue)
    del queue[0]
    children = []
    for i in range (child):
        children.append(queue[len(queue)-1-i])
    graph[key] = children
    children = []
    child = 0
    print(graph)

print(graph)


# graph = {'A': set(['B', 'C']),
#          'B': set(['A', 'D', 'E']),
#          'C': set(['A', 'F']),
#          'D': set(['B']),
#          'E': set(['B', 'F']),
#          'F': set(['C', 'E'])}

# print(graph['A'])

# graph['G'] = {'C', 'D'}

# print(graph)