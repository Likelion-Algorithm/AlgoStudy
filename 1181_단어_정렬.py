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

# data_list = ['but','but', 'i', 'wont','hesitate', 'no', 'more','no','more','it','cannot','wait','im','yours']

# 합병정렬
def mergesplit(data_list):
    if len(data_list)==1:
        return data_list
    medium = int(len(data_list)/2)    
    # 이 코드에서는 합병 정렬을 왼쪽부터 진행
    left = mergesplit(data_list[:medium])
    right = mergesplit(data_list[medium:])
    return merge(left,right)
    
def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0
    
    # case1 - left/right 둘다 있을때
    while len(left) > left_point and len(right) > right_point:
        if len(left[left_point]) == len(right[right_point]):
            # 길이가 같을 경우
            if left[left_point] == right[right_point]:
                # 문자가 같은 경우 둘중에 하나만 추가 하고 인덱스는 둘 다 1씩 추가!
                merged.append(left[left_point])
                right_point +=1
                left_point +=1
            elif left[left_point] > right[right_point]:
                # 왼쪽이 큰경우 오른쪽 추가 후 오른쪽 인덱스 하나 추가
                merged.append(right[right_point])
                right_point+=1
            elif left[left_point]<right[right_point]:
                # 오른쪽이 큰경우 왼쪽 추가 후 외쪽 인덱스 하나 추가
                merged.append(left[left_point])
                left_point+=1

        elif len(left[left_point]) > len(right[right_point]):
            merged.append(right[right_point])
            right_point += 1
        elif len(left[left_point]) < len(right[right_point]):
            merged.append(left[left_point])
            left_point += 1

    # case2 - right 데이터가 없을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1
        
    # case3 - left 데이터가 없을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1
    
    return merged

import sys
num_input = int(sys.stdin.readline())
word_list = list()
for i in range(num_input):
    word_list.append(sys.stdin.readline().strip())
for i in mergesplit(word_list):
    print(i)