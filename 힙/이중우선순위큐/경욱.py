import heapq

def solution(operations):
    
    heap=[]
    # print(heap)
    for i in operations:
        # print(heap,i)
        if i[0] == 'I':
            heapq.heappush(heap, int(i[2:]))
        elif i == "D -1":
            try:
                heapq.heappop(heap)
            except:
                continue
        else:
            try:
                heap.pop()
            except:
                continue
    if len(heap)==0:
        answer = [0,0]
        return answer
    if len(heap)==1:
        # print(heap)
        
        answer = heap*2
        return answer
    # print(heap)            
    answer = [max(heap),min(heap)]
    return answer