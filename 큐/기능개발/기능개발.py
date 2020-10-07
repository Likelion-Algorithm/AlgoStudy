import math

def solution(progresses, speeds):
    answer = []
    index = 0
    day = math.ceil((100-progresses[index])/speeds[index])
    index = 1
    answer_count = 1
    while index < len(progresses):
        temp = progresses[index]
        temp_day = math.ceil((100-progresses[index])/speeds[index])
        print(temp_day,temp,answer, answer_count,day)
        if temp_day <= day:
            answer_count +=1
            index+=1
            if index == len(progresses):
                answer.append(answer_count)
                break
        else:
            answer.append(answer_count)
            answer_count=1
            index+=1
            day = temp_day
            if index == len(progresses):
                answer.append(answer_count)
                break
    return answer