import sys
n = int(sys.stdin.readline().strip())
temp, answer, stairs = [],[],[]
for i in range(n):
    temp.append(['-','-'])
    answer.append([])
    stairs.append(int(sys.stdin.readline().strip()))
temp[0][0] = stairs[-1]
answer[0] = stairs[-1]
for i in range(1,len(stairs)):
    index = -(i+1)
    x=y=0
    if (i - 2 >=0) & (answer[i-2] != []):
        temp[i][0] = answer[i-2] + stairs[index]
        x = temp[i][0]
    if ((i - 1)>=0) & (temp[i-1][0] != '-'):
        temp[i][1] = temp[i-1][0] + stairs[index]
        y = temp[i][1]
    answer[i] = max(x,y)
print(max(answer))