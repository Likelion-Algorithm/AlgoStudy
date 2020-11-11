def solution(numbers, target):
    tmp = [0]

    for i in numbers:
        tmp_ = []
        for j in tmp:
            tmp_.append(j+i)
            tmp_.append(j-1)
        tmp = tmp_
    return tmp.count(target)
        
print(solution([1,1,1,1,1], 3))
    