def solution(n, lost, reserve):
    check = [1]*n
    check.insert(0, 0)
    check.insert(n+1, 0)

    cnt = 0

    for i in lost:
        check[i] = 0
    
    for i in reserve:
        if check[i] == 1:
            check[i] = 2
        else:
            check[i] = 1

    for i in range(1, n+1):
        if check[i] > 0:
            cnt += 1
        else:
            if check[i-1] == 2:
                check[i-1] -= 1
                check[i] += 1
                cnt += 1
            elif check[i+1] == 2:
                check[i+1] -= 1
                check[i] += 1
                cnt += 1

    return cnt

print(solution(3,[3],[1]))

#통과




