# if "ab">"ac":
#     print(True)
# elif "ab"<'ac':
#     print(False)

# if [1,-1] >[1,1]:
#     print(True)
# if [1,-1] <[1,1]:
#     print(False)


# if  "ab">"ac":
#     print(True)
# if "ab"<"ac":
#     print(False)

if '21 Junkyu' >'21 Dohyun':
    print(True)
if '21 Junkyu' < '21 Dohyun':
    print(False)
if '21 Junkyu' == '21 Dohyun':
    print('hooo')

# arr1 = [1,5,7,2,9,13,10,13,7]
# arr2 = [2,3,9,10,4,8,11,11]
# arr_1_sort={}
# arr_2_sort={}
# def solution(arr1,arr2):
#     for i in arr1:
#         for j in arr1:
#             if i == j:
#                 if j not in arr_1_sort.keys():
#                     arr_1_sort[j] = 1
#                 elif j in arr_1_sort.keys():
#                     arr_1_sort[j] += 1
#     for i in arr2:
#         for j in arr2:
#             if i == j:
#                 if j not in arr_2_sort.keys():
#                     arr_2_sort[j] = 1
#                 elif j in arr_2_sort.keys():
#                     arr_2_sort[j] += 1
            

# solution(arr1,arr2)
# if max(arr_1_sort.values())==1 and max(arr_1_sort.values())==1:
#     print(0)
# elif max(arr_1_sort.values()) < max(arr_1_sort.values()):
#     print(2)
# elif max(arr_1_sort.values()) > max(arr_1_sort.values()):
#     print(1)
# # elif max(arr_1_sort.values()) == max(arr_1_sort.values()):


# print(arr_1_sort)
# print(arr_2_sort)
# print(max(arr_1_sort))


a = [1,2,3,4,5,6]
print(len(a)//2)

# import sys
# num_input = int(sys.stdin.readline())
# num_list,weight_list  = list(),list()
# for i in range(num_input):
#     num_list.append(list(map(int,sys.stdin.readline().strip().split())))
#     weight_list.append(list(map(int,sys.stdin.readline().strip().split())))
    
# num_list = [[1, 0], [4, 2], [6, 0]]
# weight_list= [[5], [1, 2, 3, 4], [1, 1, 9, 1, 1, 1]]

# def function(num_list, weight_list):
    
#     print_index = 1
#     num_list_index = num_list[1]
#     while weight_list:
#         print(weight_list,num_list,num_list_index)
#         if max(weight_list) == weight_list[0]:
#             if num_list_index == 0:
#                 print(print_index)
#                 break
#             del weight_list[0]
#             print_index +=1
#             num_list_index-=1
#         if max(weight_list) > weight_list[0]:
#             weight_list.append(weight_list[0])
#             del weight_list[0]
#             if num_list_index == 0:
#                 num_list_index = len(weight_list)-1
#             else:
#                 num_list_index -=1
        
# for i in range(len(num_list)):
#     function(num_list[i],weight_list[i])


# c = [1,2,3,4,5,6]
# print(c[-7])
# import sys
# from _collections import defaultdict

# N = int(input())
# M = int(input())
# connected_computer = [list(map(int, sys.stdin.readline().split() ))for _ in range(M)]
# #이차원리스트로 받음

# marked = dict()
# marked = defaultdict(str) #딕셔너리 예외처리, 없는 키값을 찾아도 오류가 뜨지 않도록

# def DFS(v):
#     marked.update({v : "visited"})

#     for i in connected_computer:
#         if v in i: #정점 체크(가지 않은 정점 = 가지 않은 모서리이므로 방문해준다)
#             if marked[i[1]] != "visited":
#                 DFS(i[1])
#             elif marked[i[0]] != "visited":
#                 DFS(i[0])

# DFS(1)

a = [1,2,3]
while a :
    hoo = a.pop(0)
    print(a, hoo)
    print('여전히 실행')