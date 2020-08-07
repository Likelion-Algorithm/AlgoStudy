import sys

m, n = map(int, sys.stdin.readline().split())

box = []
queue = []
cnt = 0

box.append([1] * (m + 2))
for i in range(1, n + 1):
    box.append([1])
    for j in map(int, sys.stdin.readline().split()):
        box[i].append(j)
        if j == 1:
            queue.append((i, len(box[i]) - 1))
        elif j == -1:
            cnt+=1
    box[i].append(1)
box.append([1] * (m + 2))

cnt += len(queue)
days = 0
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while queue:
    temp = []
    days += 1
    for i in queue:
        for j in move:
            if box[i[0] + j[0]][i[1] + j[1]] == 0:
                box[i[0] + j[0]][i[1] + j[1]]=1
                temp.append((i[0] + j[0], i[1] + j[1]))
                cnt += 1
    queue = temp[:]

print([-1,days-1][cnt == m*n])
