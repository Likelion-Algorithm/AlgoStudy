from sys import stdin

num_cpt = int(input())

num_line = int(input())

graph = [[0]*num_cpt for i in range(num_cpt)]

visited = [0]

traverse_list = []

for i in range (num_line):
    cpt1, cpt2 = map(int, stdin.readline().split())
    graph[cpt1-1][cpt2-1] = 1
    graph[cpt2-1][cpt1-1] = 1

for i in range (num_cpt):
    if (graph[0][i] == 1):
        traverse_list.append(i)

while(len(traverse_list) != 0):
    print(traverse_list)
    on_traverse = traverse_list.pop()
    visited.append(on_traverse)

    for i in range (on_traverse, num_cpt):
        if (graph[on_traverse][i] == 1):
            if (i not in visited):
                traverse_list.append(i)

print(visited)
print(len(visited)-1)
