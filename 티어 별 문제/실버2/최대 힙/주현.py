import heapq

N = int(input())
heap = []
answer = []
for i in range(N):
    temp = int(input())
    if temp:
        heapq.heappush(heap, (-temp,temp))
    else:
        if heap:
            answer.append(heapq.heappop(heap)[1])
        else:
            answer.append(0)
for i in answer:
    print(i)