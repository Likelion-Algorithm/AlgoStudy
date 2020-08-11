import sys
com_num = int(sys.stdin.readline())
all_dict = dict()
for i in range(com_num):
    all_dict[i+1] = []
    
line_num = int(sys.stdin.readline())
for _ in range(line_num):
    start,end = list(map(int,sys.stdin.readline().split()))
    all_dict[start].append(end)
    all_dict[end].append(start)
def dfs(start_node, graph):
    visited , need_visit = list(),list()
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited
result = dfs(1,all_dict)[1:]

print(len(result))





# import sys
# computer_num = int(sys.stdin.readline())
# com_dict = {}
# for i in range(computer_num):
#     com_dict[i+1] = []
# double_num = int(sys.stdin.readline())
# set_1 = set()
# for i in range(double_num):
#     start,finish = list(map(int,sys.stdin.readline().split()))
#     com_dict[start].append(finish)

# result_set = set()
# def dir_search(location):
#     if len(location)== 0:
#         return 
#     else:
#         for i in location:
#             result_set.add(i)
#             dir_search(com_dict[i])
# dir_search(com_dict[1])
# print(com_dict, result_set)
# print(len(result_set))
