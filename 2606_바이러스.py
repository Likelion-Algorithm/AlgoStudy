import sys
computer_num = int(sys.stdin.readline())
com_dict = {}
for i in range(computer_num):
    com_dict[i+1] = []
double_num = int(sys.stdin.readline())
set_1 = set()
for i in range(double_num):
    start,finish = list(map(int,sys.stdin.readline().split()))
    com_dict[start].append(finish)

result_set = set()
def dir_search(location):
    if len(location)== 0:
        return 
    else:
        for i in location:
            result_set.add(i)
            dir_search(com_dict[i])
dir_search(com_dict[1])
print(com_dict, result_set)
print(len(result_set))
