import sys
temp_count = 0
num_input = int(sys.stdin.readline())
all_list = []
for i in range(num_input):
    all_list.append(list(sys.stdin.readline().strip()))

result_list = []
for row_index in range(len(all_list)):
    for column_index in range(len(all_list[row_index])):
        if all_list[row_index][column_index] == "1":
            result_list.append((row_index,column_index))

temp_count = 0
def dir_search(temp):
    global temp_count
    temp_count+=1
    if (temp[0]-1,temp[1]) in result_list:
        result_list.remove((temp[0]-1,temp[1]))
        dir_search((temp[0]-1,temp[1]))
    if (temp[0],temp[1]-1) in result_list:
        result_list.remove((temp[0],temp[1]-1))
        dir_search((temp[0],temp[1]-1))
    if (temp[0]+1,temp[1]) in result_list:
        result_list.remove((temp[0]+1,temp[1]))
        dir_search((temp[0]+1,temp[1]))    
    if (temp[0],temp[1]+1) in result_list:
        result_list.remove((temp[0],temp[1]+1))
        dir_search((temp[0],temp[1]+1))
    else:     
        return
final_list = []
final_count = 0
while len(result_list)>0:
    temp = result_list.pop(0)
    dir_search(temp)
    final_count+=1
    final_list.append(temp_count)
    temp_count = 0
print(final_count)
for i in sorted(final_list):
    print(i)





# index_set = set()
# result_list = [[]]
# def next_search(current_index):
#     print(result_list)
#     for i in result_list:
#         if (current_index[0]-1, current_index[1]) in i or (current_index[0], current_index[1]-1) in i or (current_index[0], current_index[1]+1) in i or (current_index[0]+1, current_index[1]) in i :
#             i.append(current_index)
#         if (current_index[0], current_index[1]) in i:
#             continue
#         else:
#             result_list.append([current_index])
#     # index_set.add([current_index])
    
#     if current_index[0] == len(all_list)-1:
#         return 
#     if current_index[1] == len(all_list[0])-1:
#         return
#     if all_list[current_index[0]][current_index[1]+1] == "1":
#         next_search((current_index[0],current_index[1]+1))
#     if all_list[current_index[0]+1][current_index[1]] == "1":
#         next_search((current_index[0]+1,current_index[1]))

# for row_index in range(len(all_list)):
#     for column_index in range(len(all_list)):
#         if all_list[row_index][column_index] == "1":
#             next_search((row_index,column_index))

# sorted_index_set = sorted(index_set, key = lambda x: (x[0], x[1]))
# print(sorted_index_set)


# def num_search(index_tuple):
#     print(sorted_index_set)
#     global temp_count
#     temp_count +=1
#     if (index_tuple[0]+1,index_tuple[1]) in sorted_index_set:
#         sorted_index_set.remove((index_tuple[0]+1,index_tuple[1]))
#         num_search((index_tuple[0]+1,index_tuple[1]))
#     if (index_tuple[0],index_tuple[1]+1) in sorted_index_set:
#         sorted_index_set.remove((index_tuple[0],index_tuple[1]+1))
#         num_search((index_tuple[0],index_tuple[1]+1))
#     else:
#         print(temp_count)
#         temp_count = 0





#     return
# while len(sorted_index_set) > 0 :
#     num_search(sorted_index_set.pop(0))
    

#     # if current_index[0]==0:

#     # if current_index[0]==len(all_list)-1:
#     # else: