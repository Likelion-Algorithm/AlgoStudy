# DONE
def solution(clothes):
    answer = 1
    all_clothes = {}.fromkeys([pair[1] for pair in clothes], 0)
    for pair in clothes:
        all_clothes[pair[1]] += 1
    for item in all_clothes:
        answer *= all_clothes[item]+1
    answer -= 1
    return answer
