import sys
num, column = list(map(int,sys.stdin.readline().split()))
all_list = []
for i in range(num+2):
    if i ==0 or i == num+1:
        all_list.append([0]*(column+2))
    else:
        all_list.append([0] + list(map(int,sys.stdin.readline().strip())) + [0])
loc = [1,1]
count = 1

result = []
# print(all_list)
def DFS(loc):
    # print(loc,all_list)
    # print(loc)
    global count
    if loc[0] == num and loc [1] == column:
        result.append(count)
        return 
    if all_list[loc[0]][loc[1]+1] == 1:
        # print('우')
        all_list[loc[0]][loc[1]+1] = 0
        loc[1]  +=1
        count +=1
        DFS(loc)
        all_list[loc[0]][loc[1]] = 1
        loc[1] -= 1
        count -=1
    if all_list[loc[0]+1][loc[1]] == 1:
        # print('하')
        all_list[loc[0]+1][loc[1]] = 0
        loc[0]  += 1
        count +=1
        DFS(loc)
        all_list[loc[0]][loc[1]] = 1
        loc[0] -=  1
        count -=1
    if all_list[loc[0]][loc[1]-1] == 1:
        # print('좌')
        all_list[loc[0]][loc[1]-1] = 0
        loc[1]  -= 1
        count +=1
        DFS(loc)
        all_list[loc[0]][loc[1]] = 1
        loc[1] +=  1
        count -=1
    if all_list[loc[0]-1][loc[1]] == 1:
        # print('상')
        all_list[loc[0]-1][loc[1]] = 0
        loc[0]  -= 1
        count +=1
        DFS(loc)
        all_list[loc[0]][loc[1]] = 1
        loc[0] +=  1
        count -=1
    else:
        return
DFS(loc)
print(min(result))

