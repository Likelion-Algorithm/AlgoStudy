def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for i in range(1,total+1):
        if total%i==0 and i>2:
            j = total//i
            if j*2+(i-2)*2==brown and (i-2)*(j-2)==yellow:
                if i>j:
                    answer.extend([i,j])
                else:
                    answer.extend([j,i])
                break
    return answer