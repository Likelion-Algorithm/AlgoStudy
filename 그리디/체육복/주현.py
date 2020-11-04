def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    delete=[]
    for i in lost:
        if i in reserve:
            delete.append(i)
    for i in delete:
        lost.remove(i)
        reserve.remove(i)
        
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    answer = n-len(lost)
    return answer