import heapq

def solution(operations):
    heapList = []
    for i in operations:
        oper = i.split()
        if oper[0] == "I":
            heapq.heappush(heapList,int(oper[1]))
        elif oper[1] == '-1':
            if len(heapList) > 0:
                heapq.heappop(heapList)
        else:
            if len(heapList) > 0:
                heapList = [heapq.heappop(heapList) for i in range(len(heapList)-1)]
    if len(heapList) == 0:
        answer = [0,0]
    else:
        answer = [max(heapList),min(heapList)]
    return answer