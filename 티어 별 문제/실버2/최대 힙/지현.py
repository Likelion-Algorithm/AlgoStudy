import sys
import heapq

N = int(sys.stdin.readline())
max_heap = []

for _ in range(N):
    item = int(sys.stdin.readline())

    if item == 0 and len(max_heap) == 0:
        print(0)
    else:
        if item != 0:
            heapq.heappush(max_heap, (-item, item))
        if item == 0:
            tobedeleted = heapq.heappop(max_heap)
            print(tobedeleted[1])

# 통과
# 기본적으로 heapq는 minheap!
# maxheap을 만들려면 튜블에 (-값, 값)으로 heapq에 넣어서 -값을 기준으로 minheap을 만든 후 heappop을 통해 얻은 반환값[1] 인덱스를 통해 접근!