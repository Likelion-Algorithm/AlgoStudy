# 1번) 스코빌지수 K
def solution(scoville, K):
    times = 0
    while min(scoville)<K:
        try:
            times += 1
            scoville.sort()
            scoville.append(scoville.pop(0)+(scoville.pop(0)*2))
        except IndexError:
            return -1
    return times
