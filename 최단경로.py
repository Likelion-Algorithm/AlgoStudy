import sys
spot, num = list(map(int,sys.stdin.readline().split()))
source = int(sys.stdin.readline())
all_dict = {}
exp_list = [0 for _ in range(spot+1)]
for i in range(spot):
    all_dict[i+1] = []
for i in range(num):
    start,finish,weight = list(map(int,sys.stdin.readline().split()))
    all_dict[start].append([finish,weight])
# print(all_dict)
# print(exp_list)




def func(begin):
    # print(exp_list)
    for i in all_dict[begin]:
        if i[0] == source:
            return
        if exp_list[i[0]]!=0:
            exp_list[i[0]] = min(exp_list[i[0]], i[1]+exp_list[begin])
        else:
            exp_list[i[0]]=i[1]+exp_list[begin]
        func(i[0])    
func(source)

for i in range(len(exp_list)):
    if i == 0 :
        continue
    elif i == source:
        print(0)
    elif exp_list[i] == 0:
        print("INF")
    else:
        print(exp_list[i])
# for i in range(len(exp_list)):



# 여기부터는 1부터 정점 마다의 최단 경로
# def func(begin):
#     print(exp_list)
#     if begin > spot:
#         return
#     for i in all_dict[begin]:
#         if i[0] == source:
#             return
#         if exp_list[i[0]]!=0:
#             exp_list[i[0]] = min(exp_list[i[0]], i[1]+exp_list[i[0]])
#         else:
#             exp_list[i[0]]=i[1]+exp_list[begin]
#     func(begin+1)
#     return
# func(source)

# for i in range(len(exp_list)):
#     if i == 0 :
#         continue
#     elif i == source:
#         print(0)
#     elif exp_list[i] == 0:
#         print("INF")
#     else:
#         print(exp_list[i])
# # for i in range(len(exp_list)):
