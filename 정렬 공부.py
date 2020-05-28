def bubble_sort(data_list):
    for index in range(len(data_list)):
        swap = 0
        for index2 in range(len(data_list) - 1 - index):            
            if data_list[index2] > data_list[index2 + 1]:
                data_list[index2], data_list[index2 + 1] = data_list[index2 + 1], data_list[index2]
                swap += 1
        if swap == 0:
            break
    return data_list,swap

import random 





def insertion_sort(data_list):
    for stand in range(len(data_list)):
        key = data_list[stand]
        for num in range(stand,0,-1):
            if key<data_list[num-1]:
                data_list[num-1],data_list[num]= data_list[num],data_list[num-1]
            else:
                break
    return data_list

def selection_sort(data_list):    
    for stand in range(len(data_list) ):
        lowest = stand
        for num in range(stand, len(data_list)):
            if data_list[lowest] > data_list[num]:
                lowest = num
        data_list[stand], data_list[lowest] = data_list[lowest], data_list[stand]
    return data_list




# data_list = random.sample(range(100), 10)
data_list =  [3,4,5,1,2]
def mergesplit(data_list):
    if len(data_list)==1:
        return data_list
    medium = int(len(data_list)/2)
    
    left = mergesplit(data_list[:medium])
    right = mergesplit(data_list[medium:])
    return merge(left,right)
    
    
    
def merge(left, right):
    
    
    merged = list()
    print(left,right, merged)
    left_point, right_point = 0, 0
    
    # case1 - left/right 둘다 있을때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2 - left 데이터가 없을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1
        
    # case3 - right 데이터가 없을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1
    
    return merged

print(mergesplit(data_list))

import random
data_list = random.sample(range(100),10)
def quick_sort(data_list):
    if len(data_list)<=1:
        return data_list
    left,right = list(),  list()
    pivot = data_list[0]
    for index in range(1,len(data_list)):
        if pivot > data_list[index]:
            left.append(data_list[index])
        else:
            right.append(data_list[index])
    return quick_sort(left) + [pivot] + quick_sort(right)
print(quick_sort(data_list))





