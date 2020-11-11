def solution(n, computer):
    check = [0] *len(computer[0])
    
    cnt = 0
    start = 0

    def DFS(start):
        tmp = [start]
        while tmp:
            com_start = tmp.pop()

            if check[com_start] == 0:
                check[com_start] = 1

            for i in range(len(computer[com_start])):
                if computer[com_start][i] == 1 and check[i] == 0:
                    tmp.append(i)
                   
    

    while 0 in check:
        if check[start] == 0:
            DFS(start)
            cnt += 1
        start += 1
    return cnt


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


    
