def find(possible, left, right, row, n):

    if len(row) == n-1:
        answer[0] += len(possible)
    for i in possible:
        tempLeft = []
        for j in left+[i]:
            if j - 1 < 0:
                continue
            tempLeft.append(j - 1)
        tempRight = []
        for j in right+[i]:
            if j + 1 >= n:
                continue
            tempRight.append(j + 1)
        verify = set(tempRight+tempLeft+row+[i])
        temp = [j for j in range(n) if j not in verify]
        if not temp:
            continue
        find(temp,tempLeft,tempRight,row+[i],n)




import sys

n = int(sys.stdin.readline().strip())

possible = [i for i in range(n)]
left = []
right = []
row = []
answer = [0]
find(possible,left,right,row,n)
print(answer[0])
