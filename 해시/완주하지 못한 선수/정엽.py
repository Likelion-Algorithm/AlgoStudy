from collections import defaultdict
def solution(participant, completion):
    dict1 = defaultdict(int)
    for i in participant:
        dict1[i]+=1
    for j in completion:
        dict1[j]-=1
    return sorted(dict1.items(),key =lambda x : x[1])[-1][0]