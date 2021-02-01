import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
y, x ,d= map(int, input().split())
field = []
for i in range(N):
    field.append(list(map(int, input().split())))
controller = [(0,-1),(-1, 0),(0, 1),(1, 0)]
answer = 0
def cuscal(n):
    if n==-1:
        return 3
    else:
        return n
        
def clean(x, y, d, rotate):
    global controller, answer, field

    movey = controller[d][0]
    movex = controller[d][1]

    if rotate == 4:
        if field[y+controller[(cuscal(d-1))%4][0]][x+controller[(cuscal(d-1))%4][1]]== 2 :
            clean(x+controller[(cuscal(d-1))%4][1], y+controller[(cuscal(d-1))%4][0], d , 0)
        else:
            return

    else:

        if  not field[y+movey][x+movex]:
            field[y+movey][x+movex] = 2
            answer+=1
            clean(x+movex, y+movey, (cuscal(d-1))%4, 0)
        else:
            clean(x,y,(cuscal(d-1))%4, rotate+1)

field[y][x] = 2
answer+=1
clean(x, y, d, 0)
print(answer)