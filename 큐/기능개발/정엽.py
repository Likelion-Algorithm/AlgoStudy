from math import ceil
def solution(progresses, speeds):
    answer = []
    verify,temp = ceil((100-progresses[0])/speeds[0]),1
    for x,y in list(zip(progresses[1:],speeds[1:])):
        if ceil((100-x)/y) > verify:
            verify = ceil((100-x)/y)
            answer.append(temp)
            temp = 1
        else:
            temp+=1
    answer.append(temp)
    return answer