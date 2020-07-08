import sys
def quick_sort(num_list):
    if len(num_list)<=1:
        return num_list
    left,right,mid = list(), list(), list()
    pivot = num_list[0]
    mid.append(pivot)
    for index in range(1,len(num_list)):
        if pivot > num_list[index]:
            left.append(num_list[index])
        else:
            if pivot == num_list[index]:
                mid.append(num_list[index])
            else:
                right.append(num_list[index])
    return quick_sort(left) + mid + quick_sort(right)

num_input = int(input())
num_list=[int(sys.stdin.readline()) for i in range(num_input)]
a = round(sum(num_list)/len(num_list))
num_list = quick_sort(num_list)
b = num_list[int(len(num_list)/2)]
# 최빈값
count_name = {}
result = []
for i in num_list:
    count_name[str(i)] = num_list.count(i)
for key,value in count_name.items():
    if max(count_name.values()) == value:
        result.append(int(key))
if len(result) >=2:
    result.remove(min(result))
    c = min(result)
else:
    c = max(result)
# 범위
if len(num_list)>=2:
    d = num_list[-1] - num_list[0]
else:
    d = 0
print(a)
print(b)
print(c)
print(d)

# def  getTop(list_1):
#     first_count  = 1
#     second_count = 1
#     first =  4001
#     second = 4001
#     for i in range(len(list_1)):
#         c = list_1.count(list_1[i])
#         if first > 4000:
#             first = list_1[i]
#             first_count = c
#         if first_count < c:
#             first,second  = list_1[i], first
#             first_count,second_count = c, first_count
#         if first_count > c and second_count < c :
#             second_count = c
#             second = list_1[i]
#         if second_count == c and second < list_1[i]:
#             second = list_1[i]
#             second_count = c
#     return second
# c = getTop(num_list)


# result_dict= {}
# for i in num_list:
#     result_dict[i] = num_list.count(i)
# finished = False
# t = 0
# while finished == False:
#     if max(result_dict.values())==t:
#         top = t
#         break
#     else:
#         t+=1
# final_result =[]
# for key,value in result_dict.items():
#     if value == t:
#         final_result.append(key)
# final_result.sort()
# if len(final_result) >=2:
#     c = final_result[1]
# else:
#     c = final_result[0]






# print(a)
# print(b)
# print(c)
# print(d)
