def bubblesort(str):
    for i in range(len(str), 0, -1):
        for j in range(0, i-1):
            if str[j]>str[j+1]:
                str[j],str[j+1] = str[j+1],str[j]
    return str

num = int(input())
str = []

for _ in range(num):
    str.append(int(input()))

bubblesort(str)

for i in str:
    print(i)