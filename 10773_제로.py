import sys
num_input = int(sys.stdin.readline())
num_list = list()
for i in range(num_input):
    numbers = int(sys.stdin.readline().strip())
    if numbers !=0:
        num_list.append(numbers)
    if numbers == 0:
        num_list.pop()
print(sum(num_list))







# print_index = 0
# for index in range(len(num_list)):
#     if num_list[index] == 0:
#         print_index +=1
# while 0 in num_list:
#     num_list.remove(0)
# if print_index < len(num_list):
#     print(num_list[print_index])
# else:
#     print(0)







    