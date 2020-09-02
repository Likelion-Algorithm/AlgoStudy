def find (operList, cnt, nums):
    if len(nums) == 1:
        if (operList[0] == '/') & (cnt < 0):
            cnt = -(operator[operList[0]](-cnt,nums[0]))
        else:
            cnt = operator[operList[0]](cnt,nums[0])
        return cnt, cnt
    maximum, minimum = float('-inf'), float('inf')
    newNum = nums[1:]
    for i in set(operList):
        if (i == '/') & (cnt < 0):
            tempcnt = -(operator[i](-cnt,nums[0]))
        else:
            tempcnt = operator[i](cnt,nums[0])
        x = 0
        temp = []
        for j in operList:
            if x==1 or i!=j:
                temp.append(j)
            elif i == j:
                x=1
        x, y = find(temp, tempcnt, newNum)
        maximum = max(x,maximum)
        minimum = min(y,minimum)
    return maximum, minimum

import sys

sys.stdin.readline().strip()
numList = list(map(int, sys.stdin.readline().split()))
cnt = numList[0]
numList = numList[1:]
operator = sys.stdin.readline().split()
operatorList = (['+'] * int(operator[0])) + (['-'] * int(operator[1])) + (['*'] * int(operator[2])) + (
            ['/'] * int(operator[3]))
operator = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y), '*': (lambda x, y: x * y), '/': (lambda x, y: x // y)}
maximum, minimum = find(operatorList, cnt, numList)
print(int(maximum))
print(int(minimum))



