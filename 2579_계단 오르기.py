# import sys
# num = int(sys.stdin.readline().strip())
# score_list = [0]

# for i in range(num):
#     score_list.append(int(sys.stdin.readline()))
# answer = [0, score_list[1]]    
# print(score_list)
# for i in range(1,len(score_list)):
#     print(answer)
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
            
        
def ssibal(user):
    number_1 = 3
    number_2 = 4
    a = f'{user}가 {number_1 + number_2 }개를 주문중입니다.'
    return a
jeon = ssibal('전제ㅐ현')
kang = ssibal("강경욱")
print(jeon)
print(kang)



    
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