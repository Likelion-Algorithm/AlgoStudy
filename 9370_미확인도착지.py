import sys
import heapq
test_case = int(sys.stdin.readline())
final_list = []
for _ in range(test_case):
    dot_num, line_num, cand = list(map(int,sys.stdin.readline().split()))
    start_node, need_node_start, need_node_end = list(map(int,sys.stdin.readline().split()))
    all_dict = dict()
    cand_list = list()
    for i in range(dot_num):
        all_dict[i+1] = dict()
    for _ in range(line_num):
        temp_start,temp_end,temp_weight = list(map(int,sys.stdin.readline().split()))

        all_dict[temp_start][temp_end] =temp_weight
        all_dict[temp_end][temp_start] = temp_weight
    for _ in range(cand):
        cand_list.append(int(sys.stdin.readline()))
    
    def dijk(graph,start,cand_list):
        distances = {dot:[float('inf'),0] for dot in graph}
        distances[start][0],distances[start][1] = 0, start
        queue = []
        heapq.heappush(queue,[distances[start][0],start])
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if distances[current_node][0] < current_distance:
                continue
            for adjacent, weight in graph[current_node].items():
                temp_distance = current_distance + weight
                if temp_distance < distances[adjacent][0]:
                    distances[adjacent][0] = temp_distance
                    distances[adjacent][1] =current_node
                    heapq.heappush(queue, [temp_distance, adjacent])
        result_list = []
        for i in cand_list:
            check_list = [i]
            check_start = start
            check_end = i
            while check_end != check_start:
                check_end = distances[check_end][1]
                check_list.append(check_end)
            if need_node_start in check_list and need_node_end in check_list:
                result_list.append(str(i))
        final_list.append(result_list)
    dijk(all_dict,start_node,cand_list)
for nom in final_list:
    print(" ".join(sorted(nom)))
    

    
    



    

