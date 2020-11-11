def solution(n,computers):
    answer = 0
    check = [False] * len(computers)
    def DFS(check_index):
        for i in range(len(computers[check_index])):
            if i == check_index:
                continue
            elif computers[check_index][i] == 1 and check[i] ==False :
                check[i] = True
                DFS(i)
            
    for i in range(len(computers)):
        if check[i] == False:
            DFS(i)
            answer+=1
    
    return answer

# def solution(n,computers):
#     answer = 0
#     check =[False] * len(computers)
#     for i in range(len(computersdef solution(n,computers):
    answer = 0
    check = [False] * len(computers)
    def DFS(check_index):
        for i in range(len(computers[check_index])):
            if i == check_index:
                continue
            elif computers[check_index][i] == 1 and check[i] ==False :
                check[i] = True
                DFS(i)
            
    for i in range(len(computers)):
        if check[i] == False:
            DFS(i)
            answer+=1
    
    return answer

# def solution(n,computers):
#     answer = 0
#     check =[False] * len(computers)
#     for i in range(len(computers)):
#         print(check)
#         if check[i] ==False:
#             for j in range(len(computers)):
#                 if check[j] == False:
#                     if computers[j][i] ==1:
#                         check[j] = True
#             answer+=1
#         elif check[i]==True:
#             for j in range(len(computers)):
#                 if check[j] == False:
#                     if computers[j][i]==1:
#                         check[j]=True
            
        
#     return answer

# # def solution(n, computers):
# #     answer = []
# #     def BFS():
# #         while computers:
# #             temp = computers.pop()
# #             index = len(computers)-1
# #             while  index != -1 and len(computers)!=0:
# #                 temp_list = []
# #                 for i in range(len(temp)):
# #                     print(answer, computers,temp, f'i = {i}, index = {index}')
# #                     if index == len(computers)-1 and computers[index][i]==temp[i]==1:
# #                         temp_list.append(computers.pop(index))
# #                         index-=1
# #                         break
# #                     if computers[index][i]==temp[i]==1:
# #                         temp_list.append(computers.pop(index))
# #                         break
# #                 if len(temp_list)==0:
# #                   index -=1
# #             answer.append(1)
        
# #         return answer
# #     answer = BFS()
# #     return len(answer))):
#         print(check)
#         if check[i] ==False:
#             for j in range(len(computers)):
#                 if check[j] == False:
#                     if computers[j][i] ==1:
#                         check[j] = True
#             answer+=1
#         elif check[i]==True:
#             for j in range(len(computers)):
#                 if check[j] == False:
#                     if computers[j][i]==1:
#                         check[j]=True
            
        
#     return answer

# # def solution(n, computers):
# #     answer = []
# #     def BFS():
# #         while computers:
# #             temp = computers.pop()
# #             index = len(computers)-1
# #             while  index != -1 and len(computers)!=0:
# #                 temp_list = []
# #                 for i in range(len(temp)):
# #                     print(answer, computers,temp, f'i = {i}, index = {index}')
# #                     if index == len(computers)-1 and computers[index][i]==temp[i]==1:
# #                         temp_list.append(computers.pop(index))
# #                         index-=1
# #                         break
# #                     if computers[index][i]==temp[i]==1:
# #                         temp_list.append(computers.pop(index))
# #                         break
# #                 if len(temp_list)==0:
# #                   index -=1
# #             answer.append(1)
        
# #         return answer
# #     answer = BFS()
# #     return len(answer)