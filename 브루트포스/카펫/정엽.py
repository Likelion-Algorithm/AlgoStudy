def solution(brown, yellow):
    a,b,total,answer = (lambda x,y:x%y == 0),(lambda x,y: x*2 + y*2 == brown), brown+yellow, []
    for i in range(3,total+1):
        if a(total,i) & b(i,(total//i)-2):
            answer = [max(i,total//i),min(i,total//i)]
            break
    return answer