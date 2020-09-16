# 해시 쓰지 않은 버전(정확성 통과 효율성 실패)
import sys
def solution(participant, completion):
    answer = ''
    while participant: # participant가 completion보다 반드시 하나 많으므로 반드시 답을 찾을 수 밖에 없다
        temp = participant.pop()
        if temp in completion:
            completion.remove(temp)
        else:
            answer = temp
            break
    return answer

# 프로그래머스 통과 버전
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp] #마지막 남은 temp값이 원하는 원소의 해시값

    return answer




