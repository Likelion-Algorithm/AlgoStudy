'''
다시 짜야 됨~~~
'''
def solution(tickets):
    answer, graph, START = [], {}, "ICN"
    for A, B in tickets:
        if A not in graph.keys():
            graph[A]= [[B,False]]
        else:
            graph[A].append([B,False])
            graph[A].sort(reverse = True)
    stack = [START] # graph[ICN] = [[vertex, isVisted]]
    while stack:
        A = stack.pop() # 방문한 공항이름
        answer.append(A)
        for i in range(len(graph[A])):
            if graph[A][i][1] == False and graph[A][i][0] in graph.keys():
                graph[A][i][1] = True
                stack.append(graph[A][i][0])
        if not stack:
            for i in range(len(graph[A])):
                if graph[A][i][1] == False: 
                    answer.append(graph[A][i][0])
    return answer