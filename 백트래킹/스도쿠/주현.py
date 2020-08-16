import time
start = time.time()
import sys
sdoku = []
stack = []
zero = []
for i in range(9):
    sdoku.append(list(map(int, sys.stdin.readline().split())))
for i in range(9):
    for j in range(9):
        if sdoku[i][j]==0:
            zero.append([i,j])
i,j=zero[0]
for n in range(1,10):
    change=True
    breakPoint=True
    for a in range(9):
        if sdoku[i][a]==n:
            change=False
            breakPoint=False
    if breakPoint:
        for b in range(9):
            if sdoku[b][j]==n:
                change=False
                breakPoint=False
    if breakPoint:
        for c in range((i//3)*3,(i//3)*3+3):
            for d in range((j//3)*3,(j//3)*3+3):
                if sdoku[c][d]==n:
                    change=False
                    breakPoint=False
    if change:
        stack.append([i,j,n])
x=0
y=0          
while [x,y] != zero[-1]:
    x,y,v = stack.pop()
    sdoku[x][y]=v
    for p, q in zero :
        if zero.index([p,q])>zero.index([x,y]):
            sdoku[p][q]=0
    for i, j in zero:
        if zero.index([i,j])>zero.index([x,y]):
            for n in range(1,10):
                change=True
                breakPoint=True
                for a in range(9):
                    if sdoku[i][a]==n:
                        change=False
                        breakPoint=False
                        break
                if breakPoint:
                    for b in range(9):
                        if sdoku[b][j]==n:
                            change=False
                            breakPoint=False
                            break
                if breakPoint:
                    for c in range((i//3)*3,(i//3)*3+3):
                        for d in range((j//3)*3,(j//3)*3+3):
                            if sdoku[c][d]==n:
                                change=False
                                breakPoint=False
                                break
                if change:
                    stack.append([i,j,n])
            break                  
for i in range(9):
    for j in range(9):
        print(sdoku[i][j],end=' ')
    print()
print("time :", time.time() - start)