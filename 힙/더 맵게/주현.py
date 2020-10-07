import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while 1:
        if len(scoville)==1:
            return -1
        a= heapq.heappop(scoville)
        b= heapq.heappop(scoville)
        heapq.heappush(scoville, a+2*b)
        answer += 1
        c= heapq.heappop(scoville)
        if c>=k:
            return answer
        else:
            heapq.heappush(scoville, c)
            continue