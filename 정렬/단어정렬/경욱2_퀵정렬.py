def quick_sort(data_list):
    if len(data_list)<=1:
        return data_list
    left,right = list(),  list()
    pivot = len(data_list[0])
    # 피봇 설정
    for index in range(1,len(data_list)):
        # 길이에 따른 분류
        if pivot > len(data_list[index]):
            # 피봇이 큰경우 왼쪽에
            left.append(data_list[index])
        else:
            if pivot == len(data_list[index]):
                # 길이가 같은 경우
                if data_list[0]<data_list[index]:
                    # 오름차순 정렬
                    right.append(data_list[index])
                elif data_list[0]>data_list[index]:
                    # 위와같이 오름차순 정렬후 추가
                    left.append(data_list[index])
            else: 
                # 피봇이 작은 경우 오른쪽에
                right.append(data_list[index])
    return quick_sort(left) + [data_list[0]] + quick_sort(right)

import sys
num_input = int(sys.stdin.readline())
word_list=list()
for i in range(num_input):
    word_list.append(sys.stdin.readline().strip())
# 같은 것은 set로 지워주기 set 사용해두 대나....?
# word_list = list(set(word_list))

sorted_list = quick_sort(word_list)
for i in sorted_list:
    print(i)