import sys 
num,amount = map(int, sys.stdin.readline().split())
item_list= [[0,0]]
check_list = [[0]*(amount+1)]
for _ in range(num):
    item_list.append(list(map(int,sys.stdin.readline().split())))
    check_list.append([0]*amount+[0])




for i in range(1,len(check_list)):
    for j in range(1,len(check_list[i])):
        if j >= item_list[i][0]:
            check_list[i][j] =max(check_list[i-1][j],item_list[i][1]+check_list[i-1][j-item_list[i][0]])
        else:
            check_list[i][j] = check_list[i-1][j]
print(check_list[num][amount])
# for i in range(1,len(check_list)):
#     for j in range(len(check_list[i])):        
        
#         if j+1>= item_list[i][0]:
        
#             if len(check_list[i])>= item_list[i][0]+j+1:
#                 print(f'i:{i} j:{j}')
#                 temp = item_list[i][0] + j+1
#                 check_list[i][temp-1] = max(item_list[i][1]+check_list[i-1][temp-1],check_list[i-1][temp-1])
#             else:
#                     check_list[i][j] =max(check_list[i-1][j],item_list[i][1])
#         else:
#             check_list[i][j] = check_list[i-1][j]
#         print(check_list)

        




# import sys

# num, value_amount = map(int, input().split())
# stuff = [[0,0]]
# sack = [[0 for _ in range(value_amount + 1)] for _ in range(num + 1)]



# # for _ in range(num):
# #     stuff.append(list(map(int,input().split())))
# # print(stuff)

# for i in range(1,num+1):
#     weight, value_1 = list(map(int,sys.stdin.readline().split()))
#     for j in range(1,value_amount+1):
#         print(sack, weight, value_1)
#         # weight = stuff[i][0]
#         # value_1 = stuff[i][1]
#         if j >= weight:
#             sack[i][j] = max(value_1 + sack[i-1][j-weight], sack[i-1][j])
#         else:
#             sack[i][j] = sack[i-1][j]
#         # if j < weight:
#         #     sack[i][j] = sack[i-1][j]
#         # else:
#         #     sack[i][j] = max(value_1 + sack[i-1][j-weight], sack[i-1][j])
# print(sack[num][value_amount])
# import sys 
# num,amount = list(map(int,sys.stdin.readline().split()))

# result_list = []
# for i in range(num):
#     temp_list = list(map(int,sys.stdin.readline().split()))
#     result_list_ = list(result_list)
#     if i== 0:
#         result_list.append(temp_list)
#         continue
#     else:
#         for j in result_list_:
#             if j == temp_list:
#                 continue
#             else:
#                 if j[0] + temp_list[0] <= amount:
#                     j[0] += temp_list[0]
#                     j[1] += temp_list[1]
#                 else:
#                     if temp_list not in result_list:
#                         result_list.append(temp_list)
            
# answer = max(result_list, key =lambda x : x[1])[1]
# print(answer)

    





# # item_list = []
# # weight_list = []
# # value_list = []
# # for i in range(num):
# #     a = list(map(int,sys.stdin.readline().split()))
# #     # weight, value = a
# #     # weight_list.append(weight)
# #     # value_list.append(value)
# #     item_list.append(a)


# # item_list = sorted(item_list, key = lambda x: x[0])
# # for i in item_list:
# #     weight_list.append(i[0])
# #     value_list.append(i[1])

# # answer = []
# # print(weight_list,value_list,item_list)
# # temp_weight = 0
# # temp_value = 0
# # # while temp_weight <= amount:
# # for i in range(1,len(item_list)):
# #     if sum(weight_list[-i:]) < amount:
# #         temp_weight = sum(weight_list[-i:])
# #         temp_value = sum(value_list[-i:])
# #     else:
# #         break

# # print(temp_value,temp_weight)

# # prac = [1,2,3,4]
# # for i in prac:
# #     for j in range(i,len(prac)):
# #         print(i,prac[j])