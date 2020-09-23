import math
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    tempmax = 0
    complete = [0]*n
    for i in range(n):
        complete[i]= math.ceil((100-progresses[i])/speeds[i])
    for i in range(n):
        if i==0:
            tempmax=complete[i]
            answer.append(1)
        else:
            if tempmax<complete[i]:
                tempmax=complete[i]
                answer.append(1)
            else:
                answer[-1]+=1
    return answer