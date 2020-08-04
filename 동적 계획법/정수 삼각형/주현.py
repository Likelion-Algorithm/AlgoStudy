num = int(input())
triList = list()
for i in range(num):
    triList.append(list(map(int,input().split())))

for i in range(1,num):
    for j in range(i+1):
        if j==0:
            triList[i][j] += triList[i-1][j]
        elif j==i:
            triList[i][j] += triList[i-1][j-1]
        else:
            triList[i][j] += triList[i-1][j] if triList[i-1][j]>triList[i-1][j-1] else triList[i-1][j-1]

print(max(triList[-1]))