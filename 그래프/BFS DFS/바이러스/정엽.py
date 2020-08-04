import sys
sys.stdin.readline()
m = int(sys.stdin.readline().strip())

dict1 = {}
for i in range(m):
    num1, num2 = map(int,sys.stdin.readline().split())
    if num2 != 1:
        if num1 not in dict1:
            dict1[num1] = [num2]
        else:
            if num2 not in dict1[num1]:
                dict1[num1].append(num2)
    if num1 != 1:
        if num2 not in dict1:
            dict1[num2] = [num1]
        else:
            if num1 not in dict1[num2]:
                dict1[num2].append(num1)

node = [1]
answer = []

while len(node)>0:
    temp = []
    for i in node:
        if i != 1:
            answer.append(i)
        if i not in dict1:
            continue
        temp += dict1[i]

    temp1 = []
    temp = list(set(temp))
    for i in temp:
        if (i not in answer) & (i != 1):
            temp1.append(i)
    node = temp1[:]
print(len(answer))