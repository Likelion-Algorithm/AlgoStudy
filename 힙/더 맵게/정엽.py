import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        smallNum = heapq.heappop(scoville)
        if smallNum >= K: break
        elif (len(scoville) == 0):
            answer = -1
            break
        nextSmallNum = heapq.heappop(scoville)
        heapq.heappush(scoville, smallNum+(nextSmallNum*2))
        answer+=1
    return answer