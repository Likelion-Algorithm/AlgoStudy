import time
start = time.time()  # 시작 시간 저장
 
 






import sys

col,row = map(int,sys.stdin.readline().split())

all_list = []
start_node= []
zero_count = 0
for i in range(row+2):
    
    if i == 0 or i == row+1:
        all_list.append([9] * (col+2))
    else:
        all_list.append([9]+list(map(int,sys.stdin.readline().split()))+[9])


for i in range(len(all_list)):
    for j in range(len(all_list[i])):
        if all_list[i][j] == 1:
            start_node.append(([i,j]))
        if all_list[i][j] == 0:
            zero_count +=1


def BFS(start_node, all_list):
    if zero_count == 0:
        print(0)
        return
    need_visit, visited = list(),list()
    need_visit.extend(start_node)
    count = -1
    zero_count_check = 0
    while need_visit:
        temp_list = []
        # print(need_visit)
        for i in need_visit:         
            if all_list[i[0]+1][i[1]] == 0:
                
                    all_list[i[0]+1][i[1]]=1
                    zero_count_check += 1
                    temp_list.append([i[0]+1,i[1]])
                    visited.append([i[0]+1,i[1]])
            if all_list[i[0]][i[1]+1] == 0:
                
                    all_list[i[0]][i[1]+1]=1
                    zero_count_check += 1
                    temp_list.append([i[0],i[1]+1])
                    visited.append([i[0],i[1]+1])
            if all_list[i[0]-1][i[1]] == 0:
                
                    all_list[i[0]-1][i[1]]=1
                    zero_count_check += 1
                    temp_list.append([i[0]-1,i[1]])
                    visited.append([i[0]-1,i[1]])
            if all_list[i[0]][i[1]-1] == 0:
                
                    all_list[i[0]][i[1]-1]=1
                    zero_count_check += 1
                    temp_list.append([i[0],i[1]-1])
                    visited.append([i[0],i[1]-1])
        if zero_count_check != zero_count and temp_list ==[]: 
            print(-1)
            return
        need_visit = temp_list
        count+=1
        

    # print(count,zero_count,zero_count_check)   
    print(count)
 

result = BFS(start_node,all_list)
# print(all_list)