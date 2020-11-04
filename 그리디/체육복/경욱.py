def solution(n, lost, reserve):
    answer = 0
    students = n -len(lost)
    hoo = int(len(lost))
    count = 0
    temp_lost= list(lost)
    for i in temp_lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
            students+=1
    while count !=hoo and lost:
        temp = lost.pop()

        if temp+1 in reserve:
            students+=1
            reserve.remove(temp+1)
            count+=1
        elif temp-1 in reserve:
            students+=1
            reserve.remove(temp-1)
            count +=1
    return students