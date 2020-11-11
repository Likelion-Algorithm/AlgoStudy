def solution(numbers, target):
    answer = []
    end = len(numbers)
    
    def DFS(depth, target,check,numbers):
        # print(numbers)
        if  depth == end:
            # print(check,target)
            if check == target:
                answer.append(1)
                return
            else:
                return
        temp = numbers.pop()
        for i in range(2):
            DFS(depth+1, target, [check-temp,check+temp][i==1],numbers)
        numbers.append(temp)
    DFS(0,target,0,numbers)
            
        
    return len(answer)