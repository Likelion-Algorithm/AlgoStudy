import sys

num, value = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(value + 1)] for _ in range(num + 1)]
print(knapsack)


for _ in range(num):
    stuff.append(list(map(int,input().split())))
print(stuff)

for i in range(1,num+1):
    for j in range(1,value+1):
        print(knapsack)
        weight = stuff[i][0]
        value_1 = stuff[i][1]
        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value_1 + knapsack[i-1][j-weight], knapsack[i-1][j])
print(knapsack[num][value])
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