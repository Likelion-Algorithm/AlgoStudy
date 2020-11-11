def solution(tickets):
    answer = []
    final = []
    check = [False] * len(tickets)
    def DFS(depth,stack,check,tickets):
        if depth == len(tickets) and len(answer) == len(tickets):
            answer.append(stack[0][1])
            final.append(list(answer))
            answer.pop()
            return
        for j in range(len(tickets)):
            if check[j] == False and stack[0][1] == tickets[j][0]:
                check[j] = True
                answer.append(tickets[j][0])
                DFS(depth+1, [tickets[j],j],check,tickets)
                check[j] = False
                answer.pop()
    DFS(0,[['abc','ICN'],0],check,tickets)
    return min(final)


# from collections import deque

# def solution(tickets):
#     answer = []
#     stack = [tickets[0],0]
#     check = [False] * len(tickets)
#     for i in range(len(tickets)):
#         if tickets[i][0] == "ICN" and tickets[i][1] < stack[0][1]:
#             stack = [tickets[i],i]
#     check[stack[1]] = True
#     answer.append(stack[0][0])
#     # print(check, stack)
#     while stack:
#         # print(stack)
#         temp = 0
#         for j in range(len(tickets)):
#             if check[j] == False and stack[0][1] == tickets[j][0]:
#                 if temp ==0:
#                     temp = [tickets[j], j]
#                 elif temp[0][1] > tickets[j][1]:
#                     temp = [tickets[j],j]
#         if temp :
#             stack = temp
#             check[temp[1]] = True
#             answer.append(temp[0][0])
#         else:
#             answer.append(stack[0][1])
#             return answer

    
            
#     check = [False] * len(tickets)
#     while dequee:
#         temp = dequee.popleft()
#         answer.append(temp[0])
#         temp_list = list()
#         for i in range(len(tickets)):
#             if temp[1] == tickets[i][0] and check[i] != True:
#                 temp_list.append(tickets[i])
#                 check[i] = True
                
#         temp_list.sort(key = lambda x : x[1][0])
#         print(temp_list)
#         dequee.extend(temp_list)
#         print(dequee)
        
        
        
    