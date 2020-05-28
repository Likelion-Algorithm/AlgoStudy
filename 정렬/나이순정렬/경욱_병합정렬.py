# 합병 정렬
def mergesplit(data_list):
    if len(data_list)==1:
        return data_list
    medium = int(len(data_list)/2)
    left = mergesplit(data_list[:medium])
    right = mergesplit(data_list[medium:])
    return merge(left,right)
def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0
    # case1 - left/right 둘다 있을때
    while len(left) > left_point and len(right) > right_point:
        if int(left[left_point].split()[0]) == int(right[right_point].split()[0]):
            # 나이가 같을 때 어차피 먼저 가입한 회원은 항상 왼쪽이므로 그냥 왼쪽 추가하고 인덱스 추가!
            merged.append(left[left_point])
            left_point += 1
            
        elif int(left[left_point].split()[0]) < int(right[right_point].split()[0]):
            # 나이가  오른쪽이 클  때 왼쪽 추가 

            merged.append(left[left_point])
            left_point +=1
        elif int(left[left_point].split()[0]) > int(right[right_point].split()[0]): 
            # 나이가 왼쪽이 클 때 오른쪽 추가 
            merged.append(right[right_point])
            right_point+=1
        

    # case2 - left 데이터가 없을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1
        
    # case3 - right 데이터가 없을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1
    
    return merged

# member_list = ['21 Junkyu', "21 Dohyun", '20 Sunyoung', '20 abc', '23 hooah', '123 abc', '111 bca','111 a']
import sys
num_input = int(sys.stdin.readline())
word_list = list()
for i in range(num_input):
    word_list.append(sys.stdin.readline().strip())
for i in mergesplit(member_list):
    print(i)
