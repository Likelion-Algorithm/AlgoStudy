import sys
vertex, edge = list(map(int, sys.stdin.readline().split()))
graph = dict()
need_visit = []
check = []
for i in range(vertex):
    graph[i+1] = []
    need_visit.append(i+1)
    check.append(False)
for i in range(edge):
    begin, end = list(map(int, sys.stdin.readline().split()))
    graph[begin].append(end)
    graph[end].append(begin)


def sol(graph, need_visit, check):
    count = 0
    stack = []
    while need_visit:
        dlt = need_visit.pop()
        stack.append(dlt)
        check[dlt-1] = True
        while stack:
            # print(need_visit, check, graph, stack)
            temp = stack.pop()
            for i in graph[temp]:
                if check[i-1] == False:
                    check[i-1] = True
                    need_visit.remove(i)
                    stack.append(i)
        count += 1
    return count


print(sol(graph, need_visit, check))
