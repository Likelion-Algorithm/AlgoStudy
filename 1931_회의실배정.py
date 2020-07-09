import sys
num_input = int(sys.stdin.readline())
all_list = []
for i in range(num_input):
    count  = 0 
    temp_list = []
    temp = list(map(int,sys.stdin.readline().split()))
    for j in range(temp[0],temp[1]+1):
        temp_list.append(j)
    all_list.append(temp_list)

