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