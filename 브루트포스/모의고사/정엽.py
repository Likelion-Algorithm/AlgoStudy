def solution(answers):
    first, second, third =list(map(int,'12345'*2000)), list(map(int,'21232425'*1250)), list(map(int,'3311224455'*1000)) #문제가 10000개니까
    tempAnswer = [0,0,0]
    for i in range(len(answers)):
        if first[i] == answers[i]: tempAnswer[0]+=1
        if second[i] == answers[i]: tempAnswer[1] += 1
        if third[i] == answers[i]: tempAnswer[2] += 1
    answer = [i+1 for i in range(3) if tempAnswer[i] == max(tempAnswer)]  
    return answer