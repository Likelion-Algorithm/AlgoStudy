import sys
num_input = int(sys.stdin.readline())
num_list = []
for i in range(num_input):
    num_list.append(list(map(int,sys.stdin.readline().split())))




for i in range(1,len(num_list)):
    dis = len(num_list[i])
    for j in range(dis):
        if j == 0:
            num_list[i][j] = num_list[i][j] + num_list[i-1][0]
        elif j == dis-1:
            num_list[i][j] = num_list[i][j] + num_list[i-1][-1]
        else:
            num_list[i][j] = max(num_list[i][j]+num_list[i-1][j-1],num_list[i][j]+num_list[i-1][j])
print(max(num_list[-1])) 

        
        

 



#         if num_list[i+1][j] > num_list[i+1][j+1]:
#             count += num_list[i+1][j]
#             print(count)
#         else:
#             count+=num_list[i+1][j+1]


# print(num_list)