import sys 
num = int(sys.stdin.readline())
all_list = []

for _ in range(num):
    all_list.append(list(map(int,sys.stdin.readline().split())))
team_check_list = [False] * (num)
result_list = []
# print(team_check_list)
calc_list = []
high_score = 0
def DFS(depth, result_list,index,team_check_list):
    # print(result_list,team_check_list,depth)
    if depth == num//2:
        a_count = 0
        b_count = 0
        # for i in range(num//2):
        #     for j in range(i+1, num//2):
        #         a_count +=  all_list[result_list[i]][result_list[j]]+all_list[result_list[j]][result_list[i]]
        #         b_count += all_list[num-result_list[]]
        calc_list.append(list(result_list))
        
        return
    else:
        for i in range(index,num):
            if team_check_list[i] == False:
                result_list.append(i)
                team_check_list[i] = True
                index = i
                DFS(depth+1, result_list, index,team_check_list)
                result_list.pop()
                team_check_list[i] =False
                
def calc_score(calc_list):
    smallest = 10000
    for i in range(len(calc_list)//2):
        temp_count_a= 0
        temp_count_b= 0
        for j in range(len(calc_list[i])):
            for k in range(j+1,len(calc_list[i])):
                a_1 = calc_list[i][j]
                a_2 = calc_list[i][k]
                b_1 = calc_list[-i-1][j]
                b_2 = calc_list[-i-1][k]
                temp_count_a+=all_list[a_1][a_2]+all_list[a_2][a_1]
                temp_count_b  += all_list[b_1][b_2]  +all_list[b_2][b_1]
                # print(calc_list[i][j],calc_list[i][k])
        if smallest > abs(temp_count_a-temp_count_b):
            smallest = abs(temp_count_a-temp_count_b)
        # print(calc_list[i],calc_list[-i-1])
    return smallest

DFS(0,result_list,0,team_check_list)
# print(calc_list)
print(calc_score(calc_list))





# import sys
# num = int(sys.stdin.readline())
# all_list = []
# # for _ in range(num):
# #     all_list.append(list(map(int,sys.stdin.readline().split())))
# # print(all_list)
# team_list = [True]+[False]*(num-1)
# result_list = [0]
# team_done = []
# result = 0
# cal_check_result = []
# cal_check_list = [False]*(num//2)
# # def calc(cal_num,depth,result_list,all_list,index):
#     # for i in range(len(result_list)):
#     #     for j in range(i+1,len(result_list)):
#     #         print(i,j)



#     # if depth== 2:
#     #     print(cal_check_result)
#     # for i in range(index,len(result_list)):
#     #     if cal_check_list[i] == False:
#     #         cal_check_result.append(result_list[i])
#     #         cal_check_list[i] =True
#     #         index = i
#     #         calc(num//2, depth+1, result_list,all_list,index)
#     #         cal_check_result.pop()
#     #         cal_check_list[i] = False

# def DFS(num,depth, team_list, result_list,index,all_list):
#     print(result_list)
#     # if num//2 == depth:
#     #     print(result_list, 'result_list')
#     #     team_done.append(result_list)
#     if num == depth:
#         team_done.append(result_list[:num//2])
#         team_done.append(result_list[num//2:])
#         # calc(num//2, 0, team_done,all_list,0)
#         print(team_done,result_list)
#         return
#     else:
#         for i in range(index,num):
#             if team_list[i]==False :
#                 result_list.append(i)
#                 team_list[i]=True
#                 index = i
#                 DFS(num,depth+1,team_list,result_list,index+1,all_list)
#                 result_list.pop()
#                 team_list[i]=False
    
# DFS(num,1,team_list,result_list,1,all_list)

        
