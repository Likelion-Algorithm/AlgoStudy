def regre(now, target, words, count):
    minimum = float("inf")
    if now == target:
        return count
    if len(words) == 0:
        return float("inf")
    for i in words:
        verify = 0
        for j in range(len(i)):
            if i[j] == now[j]:
                verify += 1
        if verify == len(i) - 1:
            minimum = min(minimum, regre(i, target, words[:words.index(i)] + words[words.index(i) + 1:], count + 1))
    return minimum


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = regre(begin, target, words, 0)
    if not answer:
        return 0
    return answer