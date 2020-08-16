import sys
num = int(sys.stdin.readline())
all_list = [0]
for _ in range(num):
    all_list.append(int(sys.stdin.readline()))
print(all_list)

# import sys
# num = int(sys.stdin.readline().strip())
# score_list = [0]

# for i in range(num):
#     score_list.append(int(sys.stdin.readline()))
# answer = [0, score_list[1]]    
# print(score_list)
# for i in range(1,len(score_list)):
#     print(answer)2
#     if i == 0 or i ==1 :
#         continue
#     if i ==2 :
#         answer.append(score_list[i-1] + score_list[i])
#     else:
#         if score_list[i]+answer[i-2] > score_list[i]+answer[i-1]:
#             answer.append(score_list[i]+answer[i-2])
#         else:
#             answer.append(score_list[i]+answer[i-1])
# print(answer)
            



    
# count_list = [[score_list[-1],0,-1]]

# index = -1
# move_count =0
# result_list = [ ]
# while index > -len(score_list):
#     temp_list = []
#     for i in count_list:
#         if i[2] <= -len(score_list):
#             result_list.append(i)
#             continue
#         if i[2] == -len(score_list)+1:
#             temp_list_3 = [i[0]+score_list[0],0,0]
#             result_list.append(i)
#             continue
#         if i[1] >=2  and i[2] >= -len(score_list)+2 :
#             temp_list_4 = [i[0]+score_list[i[2]-2], 0,i[2]-2]
#             temp_list.appen(temp_list_4)
#             continue
#         if i[1]>=2 and i[2]< -len(score_list)+2:
#             result_list.append(i)
#             continue
#         else:
#             temp_list_1 = [i[0]+score_list[i[2]-1],i[1]+1,i[2]-1]
#             temp_list_2 = [i[0]+score_list[i[2]-2], 0,i[2]-2]
#             temp_list.append(temp_list_1)
#             temp_list.append(temp_list_2)
#     count_list = temp_list
#     index -= 1
    

# print(result_list)