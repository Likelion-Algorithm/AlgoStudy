from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer, truck_weights = 1, deque(truck_weights)
    tempList, sum = deque(), 0
    while len(truck_weights)>0:
        while sum + truck_weights[0] <= weight:
            answer += 1
            for i in tempList:
                i[1] += 1
            num = truck_weights.popleft()
            tempList.append([num,1])
            sum += num
            if not truck_weights:
                break
        first = tempList.popleft()
        answer+=[0,bridge_length - first[1]][bridge_length-first[1]>=0]
        sum-=first[0]
        for i in tempList:
            i[1] += [0,bridge_length - first[1]][bridge_length-first[1]>=0]

    while tempList:
        num = tempList.popleft()
        answer += [0, bridge_length - num[1]][bridge_length - num[1] >= 0]
        for i in tempList:
            i[1] += [0,bridge_length - num[1]][bridge_length-num[1]>=0]

    return answer