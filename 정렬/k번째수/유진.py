# 1번) K번째 수
def solution(array, commands):
    answer = []
    for s in commands:
        answer.append(sorted(array[s[0]-1:s[1]])[s[2]-1])
    return answer
