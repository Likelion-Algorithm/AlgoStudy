def solution(prices):
    result= [0]*len(prices)
    
    for i in range(len(prices)-1):
        temp = i+1
        count = 0
        while temp < len(prices):
            count +=1
            if prices[temp] >= prices[i]:
                result[i] = count
            else:
                result[i] = count 
                break
            temp +=1
        
    
    return result