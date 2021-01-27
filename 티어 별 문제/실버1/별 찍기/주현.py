N = int(input())
answer = []
for i in range(N):
    answer.append([' ']*N)

def star(i,j,n):
    global answer
    if n==1:
        answer[i][j] = "*"
        return
    else:
        star(i,j,n//3)
        star(i,j+(n//3),n//3)
        star(i,j+(n//3)*2,n//3)
        star(i+(n//3),j,n//3)
        star(i+(n//3),j+(n//3)*2,n//3)
        star(i+(n//3)*2,j,n//3)
        star(i+(n//3)*2,j+(n//3),n//3)
        star(i+(n//3)*2,j+(n//3)*2,n//3)

star(0,0,N)
for i in answer:
    for j in i:
        print(j, end='')
    print()


