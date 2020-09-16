def solution (clothes):
    check_dict = dict()
    for i in clothes:
        try:
            check_dict[i[1]].append(i[0])
        except:
            check_dict[i[1]] = list()
            check_dict[i[1]].append(i[0])
    answer = 1
    for i in check_dict:
        answer *= len(check_dict[i])+1

    return answer-1
    
