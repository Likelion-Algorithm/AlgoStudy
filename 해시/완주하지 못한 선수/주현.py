def solution(participant, completion):
    p = dict()
    for i in participant:
        if i not in p.keys():
            p[i]= 1
        else:
            p[i]+=1
    for j in completion:
        p[j]-= 1
    for k in p.keys():
        if p[k]==1:
            answer = k
            return answer