def selectionsort(str):
    for i in range(len(str), 0, -1):
        max = 0 #가장 큰 값의 인덱스를 설정
        for j in range(0, i):
            if str[j]>str[max]:
                max = j #큰 값이 나타나면 해당 값으로 max 변경
        str[max], str[j] = str[j], str[max] # 가장 큰 값이 맨 뒤로 옮겨감
    return str

num = int(input())
str = []

for i in range(num):
    str.append(int(input()))

selectionsort(str)

for i in str:
    print(i)