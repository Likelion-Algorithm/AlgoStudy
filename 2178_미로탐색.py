import sys
row,col = list(map(int,sys.stdin.readline().split()))
all_list = []
for i in range(row+2):
    if i == 0 or i == row+1:
        all_list.append([0] * (col+2))
    else:
        all_list.append([0]+list(map(int,sys.stdin.readline().strip()))+[0])

start = [1,1]

def BFS(start_node,graph):
    count = 1
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    visited.append(start_node)
    while [row,col] not in visited :
        temp_need_list = list(need_visit)
        temp_list = []
        count +=1
        while temp_need_list:
            try:
                i = need_visit.pop(0)
                if all_list[i[0]+1][i[1]] == 1:
                    if [i[0]+1,i[1]] not in visited:
                        temp_list.append([i[0]+1,i[1]])
                        visited.append([i[0]+1,i[1]])
                if all_list[i[0]][i[1]+1] == 1:
                    if [i[0],i[1]+1] not in visited:
                        temp_list.append([i[0],i[1]+1])
                        visited.append([i[0],i[1]+1])
                if all_list[i[0]-1][i[1]] == 1:
                    if [i[0]-1,i[1]] not in visited:
                        temp_list.append([i[0]-1,i[1]])
                        visited.append([i[0]-1,i[1]])
                if all_list[i[0]][i[1]-1] == 1:
                    if [i[0],i[1]-1] not in visited:
                        temp_list.append([i[0],i[1]-1])
                        visited.append([i[0],i[1]-1])
            except IndexError:
                break
        
        
        need_visit.extend(temp_list)
    print(count)
    return visited
result = BFS(start,all_list)






# import sys
# num, column = list(map(int,sys.stdin.readline().split()))
# all_list = []
# for i in range(num+2):
#     if i ==0 or i == num+1:
#         all_list.append([0]*(column+2))
#     else:
#         all_list.append([0] + list(map(int,sys.stdin.readline().strip())) + [0])
# loc = [1,1]
# count = 1



# # 여기서부터=는 시간 초과 코드
# result = []
# # print(all_list)
# def DFS(loc):
    
#     # print(loc,all_list)
#     # print(loc)
#     global count
#     if loc[0] == num and loc [1] == column:
#         result.append(count)
#         return 
#     if all_list[loc[0]][loc[1]+1] == 1:
#         # print('우')
#         all_list[loc[0]][loc[1]+1] = 0
#         loc[1]  +=1
#         count +=1
#         DFS(loc)
#         all_list[loc[0]][loc[1]] = 1
#         loc[1] -= 1
#         count -=1
#     if all_list[loc[0]+1][loc[1]] == 1:
#         # print('하')
#         all_list[loc[0]+1][loc[1]] = 0
#         loc[0]  += 1
#         count +=1
#         DFS(loc)
#         all_list[loc[0]][loc[1]] = 1
#         loc[0] -=  1
#         count -=1
#     elif all_list[loc[0]][loc[1]-1] == 1:
#         # print('좌')
#         all_list[loc[0]][loc[1]-1] = 0
#         loc[1]  -= 1
#         count +=1
#         DFS(loc)
#         all_list[loc[0]][loc[1]] = 1
#         loc[1] +=  1
#         count -=1
#     elif all_list[loc[0]-1][loc[1]] == 1:
#         # print('상')
#         all_list[loc[0]-1][loc[1]] = 0
#         loc[0]  -= 1
#         count +=1
#         DFS(loc)
#         all_list[loc[0]][loc[1]] = 1
#         loc[0] +=  1
#         count -=1
#     else:
#         return
# DFS(loc)
# print(min(result))

