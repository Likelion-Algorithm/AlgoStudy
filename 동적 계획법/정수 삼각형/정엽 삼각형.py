import sys

n = int(sys.stdin.readline().strip())
answer = [0]*n
triangle = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
answer = [triangle[0][0]]
for i in range(len(triangle)-1):
    temp=[]
    for j in range(len(triangle[i])):
        value1 = answer[j]+triangle[i+1][j]
        value2 = answer[j]+triangle[i+1][j+1]
        if j == 0:
            temp.append(value1)
            temp.append(value2)
        else:
            if value1 > temp[j]:
                temp[j] = value1
            temp.append(value2)
    answer = temp[:]
print(max(answer))