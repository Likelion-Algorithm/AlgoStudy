import sys
num_input = list(map(int,sys.stdin.readline().strip().split()))

num_list = [i+1 for i in range(num_input[0])]
num_index = num_input[1]
delete_list = list(map(int,sys.stdin.readline().strip().split()))
 
move_index =0
while delete_list:
    if num_list[0] == delete_list[0]:
        del delete_list[0], num_list[0]
    elif num_list.index(delete_list[0]) <= len(num_list)//2:
        num_list.append(num_list[0]) 
        del num_list[0]
        move_index+=1
    elif num_list.index(delete_list[0]) > len(num_list)//2:
        num_list.insert(0,num_list[-1])
        del num_list[-1]
        move_index+=1


print(move_index)
    
