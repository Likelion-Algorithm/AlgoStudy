import sys

sys.stdin.readline()
m = int(sys.stdin.readline().strip())

dict1 = {}
for i in range(m):
    num1, num2 = map(int, sys.stdin.readline().split())
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

stack = [1]
answer = []

while len(stack) > 0:
    temp = stack.pop()
    if temp not in dict1:
        continue
    a = dict1[temp]
    for i in a:
        if i in answer:
            continue
        stack.append(i)
        answer.append(i)

print(len(answer))
