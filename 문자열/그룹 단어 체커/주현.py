num = int(input())
source = list()
answer = 0
for i in range(num):
    source.append(input())
for i in source:
    result = True
    temp = ''
    chars = set()
    for char in i:
        if temp !=char and char in chars:
            result = False
        chars.add(char)
        temp = char
    if result:
        answer+=1
print(answer)