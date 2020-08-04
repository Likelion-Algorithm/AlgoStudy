import sys
num,amount = list(map(int,sys.stdin.readline().split()))





# item_list = []
# weight_list = []
# value_list = []
# for i in range(num):
#     a = list(map(int,sys.stdin.readline().split()))
#     # weight, value = a
#     # weight_list.append(weight)
#     # value_list.append(value)
#     item_list.append(a)


# item_list = sorted(item_list, key = lambda x: x[0])
# for i in item_list:
#     weight_list.append(i[0])
#     value_list.append(i[1])

# answer = []
# print(weight_list,value_list,item_list)
# temp_weight = 0
# temp_value = 0
# # while temp_weight <= amount:
# for i in range(1,len(item_list)):
#     if sum(weight_list[-i:]) < amount:
#         temp_weight = sum(weight_list[-i:])
#         temp_value = sum(value_list[-i:])
#     else:
#         break

# print(temp_value,temp_weight)

# prac = [1,2,3,4]
# for i in prac:
#     for j in range(i,len(prac)):
#         print(i,prac[j])