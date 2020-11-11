from itertools import combinations
def solution(numbers, target):
    answer = 0; plus_index_list = []
    for i in range(1, len(numbers)+1):
        plus_index_list += list(combinations(range(len(numbers)), i))
    for plus_index in plus_index_list:
        sum = 0
        for i in range(len(numbers)):
            sum += [-numbers[i], numbers[i]][i in plus_index]
        answer += [0, 1][sum == target]
    return answer