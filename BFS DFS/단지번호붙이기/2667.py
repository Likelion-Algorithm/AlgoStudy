from _collections import defaultdict
N = int(input())
houseNum = [list(map(int, str(input()))) for _ in range(N)]
a = list()
for i in range(N):
    for j in range(N):
        if houseNum[i][j] == 1:
            try:
                if houseNum[i][j+1] == 1:
                    a.append([(i, j),(i,j+1)])
                if houseNum[i+1][j] == 1:
                    a.append([(i+1, j),(i,j)])
            except IndexError:
                continue


print(a)


marked = dict()
marked =defaultdict(int)

def DFS(v):
    marked.update({v : "visited"})

    for i in a:
        if v in i: #정점 체크(가지 않은 정점 = 가지 않은 모서리이므로 방문해준다)
            if marked[i[1]] != "visited":
                q = i[1]
                a.remove(i)
                DFS(q)

            elif marked[i[0]] != "visited":
                q = i[0]
                a.remove(i)
                DFS(q)
    if len(a) > 0:

        DFS(a[0][0])


DFS(a[0][0])
print(marked)
print(a)
