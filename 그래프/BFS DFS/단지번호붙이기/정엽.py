import sys
n = int(sys.stdin.readline().strip())
list1 = []
check = {}
for i in range(n):
    check[i] = []
    list1.append([])
    for j in sys.stdin.readline().strip():
        list1[i].append(int(j))

answer = []

for i in range(n):
    for j in range(n):
        if j in check[i]:
            continue
        cnt = 0
        if (list1[i][j] == 1) & (j not in check[i]):
            stack = [[i,j]]
            check[i].append(j)
            cnt+=1
            while len(stack) != 0:

                temp = []
                for x in stack:
                    # if (x[0]+1) <= n or (x[0]+1)<0:
                    #     None
                    if ((x[0]+1) < n) & ((x[0]+1) >= 0):
                        if (list1[x[0]+1][x[1]] == 1) & (x[1] not in check[x[0]+1]):
                            temp.append([x[0]+1,x[1]])
                            check[x[0]+1].append(x[1])
                            cnt+=1
                    # if (x[0] -1) <= n or (x[0] - 1) < 0:
                    #     None
                    if ((x[0]-1)< n) & ((x[0]-1)>=0):
                        if  (list1[x[0]-1][x[1]] == 1) & (x[1] not in check[x[0]-1]):
                            temp.append([x[0]-1, x[1]])
                            check[x[0]-1].append(x[1])
                            cnt+=1
                    # if (x[1] + 1) <= n or (x[1] + 1) < 0:
                    #     None
                    if ((x[1]-1) < n) & ((x[1]-1) >= 0):
                        if (list1[x[0]][x[1]-1] == 1) & ((x[1]-1) not in check[x[0]]):
                            temp.append([x[0], x[1]-1])
                            check[x[0]].append(x[1]-1)
                            cnt+=1
                    # if (x[1] - 1) <= n or (x[1] - 1) < 0:
                    #     None
                    if ((x[1]+1) < n) & ((x[1]+1) >=0):
                        if (list1[x[0]][x[1]+1] == 1) & ((x[1]+1) not in check[x[0]]):
                            temp.append([x[0], x[1]+1])
                            check[x[0]].append(x[1]+1)
                            cnt+=1

                stack = temp[:]
            answer.append(cnt)
print(len(answer))
for i in sorted(answer):
    print(i)






