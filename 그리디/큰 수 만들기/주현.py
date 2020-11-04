from collections import deque
def solution(number, k):
    answer = ''
    number = list(map(int,number))
    length = len(number)
    number = deque(number)
    while k!=0 and length!=k:
        n = 0
        for i in range(k+1):
            if number[i]==9:
                n=i
                break
            elif number[i]>number[n]:
                n=i
        #n= number.index(max(number[0:k+1]))
        #number=number[n:]
        for i in range(n):
            number.popleft()
            length-=1
        answer+=str(number.popleft())
        length-=1
        k-=n
    if len(number)==k:
        return answer
    else:
        for i in number:
            answer+=str(i)
    return answer