import sys
N, M = sys.stdin.readline().split()
N = int(N)
M = int(M)
# all_list = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

all_list = list()

for j in range(N):
    x = [int(x) for x in list(sys.stdin.readline().strip())]
    x.insert(0,0)
    x.append(0)
    all_list.append(x)

pre_list = [0]*(M+2)
post_list = [0]*(M+2)
all_list.insert(0, pre_list)
all_list.append(post_list)

print(all_list)


v_list = list()
for i in all_list:
    x = list()
    for j in i:
        x.append(False)
    v_list.append(x)
print(v_list)

# for i in range(N):
#     for j in range(M):
#         if all_list[i][j] == 1:
#             v_list[i][j] = True
#
# print(v_list)

cnt = 1
i, j = 1,1

def find_way(x, y):
    global cnt
    if x == N and y == M: return (x,y)

    v_list[x][y] = True
    #     return False
    if all_list[x][y] == 1:
        if v_list[x+1][y] == False and v_list[x][y+1] == False:
            try_down = find_way(x+1, y)
            if try_down == True:
                return True


            try_east = find_way(x, y+1)
            if try_east == True:
                return try_east


            try_up = find_way(x-1, y)
            return try_up
        else:
            return False
    else:
        return False



print(find_way(1,1), cnt)




