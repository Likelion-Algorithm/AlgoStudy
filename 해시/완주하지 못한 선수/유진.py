def solution(participant, completion):
    for t in list(zip(sorted(participant), sorted(completion))):
        print(t)
        if t[0]!=t[1]: return t[0]
    return sorted(participant)[-1]
