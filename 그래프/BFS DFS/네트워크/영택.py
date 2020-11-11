def solution(n, computers):
    answer = 0; visited = [False] * n
    stack = [computers[0]]; visited[0] = True
    while stack:
        elem = stack.pop()
        for i in range(len(elem)):
            if elem[i] == 1 and visited[i] == False:
                visited[i]= True
                stack.append(computers[i])
        answer += [0, 1][not stack]
        if not stack and False in visited:
            i = visited.index(False); stack.append(computers[i])
    return answer