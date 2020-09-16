def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            answer = participant[i]   
            return answer
        elif participant[i] == completion[i]:
            continue
    answer =participant[-1] 
    return answer