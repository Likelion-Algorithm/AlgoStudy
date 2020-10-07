import heapq
def solution(operations):
    queue = []
    heapq.heapify(queue)
    answer = []
    for i in operations:
        if i[0]=='I':
            temp = i[1:]
            heapq.heappush(queue, int(temp))
        else:
            if i[2]=='1' and queue:
                queue.pop(queue.index(max(queue)))
            elif i[2]=='-' and queue:
                heapq.heappop(queue)
    if queue:
        answer.append(queue.pop(queue.index(max(queue))))
        answer.append(heapq.heappop(queue))
    else:
        answer = [0,0]
    return answer