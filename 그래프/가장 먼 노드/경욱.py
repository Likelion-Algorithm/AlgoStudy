def solution (n,edge):
    answer = 0
    check = [False] * n
    temp_list = [1]
    check[0] = True
    graph = dict()
    for i in range(len(edge)):
        if edge[i][0] in graph:
            graph[edge[i][0]].append(edge[i][1])
        if edge[i][1] in graph:
            graph[edge[i][1]].append(edge[i][0])
        if edge[i][0] not in graph:
            graph[edge[i][0]]=[edge[i][1]]
        if edge[i][1] not in graph:
            graph[edge[i][1]]=[edge[i][0]]
            
    while temp_list:
        # print(temp_list)
        temp_add_list = []
        for i in temp_list:
            for j in graph[i]:
                if check[j-1] == False:
                    temp_add_list.append(j)
                    check[j-1] = True
        temp_list = list(temp_add_list)
        if temp_list ==[]:
            continue
        else:
            answer = len(temp_list)

    return answer
# def solution(n, edge):
#     answer = 1
#     check = [False] * n
#     # edge.sort(key = lambda x : (x[0],x[1]), reverse=True)
#     temp_list = [1]
#     check[0] = True
#     while edge:
#         temp_add_list = []
#         for i in range(len(temp_list)):
#             temp = temp_list[i]
#             check_index = 0
#             while check_index <= len(edge)-1:
#                 print(temp_list, edge, check_index)
#                 if edge[check_index][0] == temp:
#                     if check[edge[check_index][1]-1] == False: 
#                         temp_add_list.append(edge[check_index][1])
#                         check[edge[check_index][1]-1] = True
#                     del edge[check_index]
#                 elif edge[check_index][1]==temp:
#                     if check[edge[check_index][0]-1] == False:
#                         temp_add_list.append(edge[check_index][0])
#                         check[edge[check_index][0]-1] = True
#                     del edge[check_index]
#                 else:
#                     check_index +=1
#         temp_list = list(temp_add_list)
#         if temp_list ==[]:
#             continue
#         else:
#             answer = len(temp_list)
        
#     return answer
    # while edge:
    #     temp_add_list = set()
    #     while temp_list:
    #         temp_list.sort(reverse=True)
    #         temp = temp_list.pop()
    #         while temp == edge[-1][0] or temp == edge[-1][1]:
    #             if temp == edge[-1][0] and check[edge[-1][1]-1] ==False:
    #                 check[edge[-1][1]-1] = True
    #                 temp_add_list.add(edge.pop()[1])
    #             if temp == edge[-1][1] and check[edge[-1][0]-1] ==False:
    #                 check[edge[-1][0]-1] = True
    #                 temp_add_list.add(edge.pop()[0])
    #     temp_list = list(temp_add_list)
        
            
#     print(edge)
#     return answer