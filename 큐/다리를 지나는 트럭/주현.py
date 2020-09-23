def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = []
    sumOnBridge = 0
    truck_weights.reverse()
    while sumOnBridge!=0 or len(onBridge)!=bridge_length:
        if len(onBridge)==bridge_length:
            sumOnBridge -= onBridge.pop(0)
            if not truck_weights or sum(onBridge)+truck_weights[-1]>weight:
                onBridge.append(0)
            else:
                temp = truck_weights.pop()
                sumOnBridge += temp
                onBridge.append(temp)
            answer+=1
        else:
            if not truck_weights or sumOnBridge + truck_weights[-1]>weight:
                onBridge.append(0)
            else:
                temp = truck_weights.pop()
                sumOnBridge += temp
                onBridge.append(temp)
            answer+=1
    return answer