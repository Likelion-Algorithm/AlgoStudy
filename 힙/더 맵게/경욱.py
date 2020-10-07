import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville)!=1:
        
        temp_1 = heapq.heappop(scoville)
        temp_2 = heapq.heappop(scoville)
        if temp_1 >= K:
            return answer 
        # print(scoville , temp_1, temp_2)
        temp_amount = temp_1 + (temp_2*2)
        heapq.heappush(scoville,temp_amount)
        answer+=1
        if len(scoville)==1 and temp_amount < K:
            answer = -1
            return answer
            
        
        
        # print(scoville.pop())
    
    return answer