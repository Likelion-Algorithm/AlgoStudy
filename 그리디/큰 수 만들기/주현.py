from collections import deque
def solution(number, k):
    answer = ''
    number = list(map(int,number))
    length = len(number)
    number = deque(number)
    while k!=0 and length!=k:
        n = 0
<<<<<<< HEAD
        for i in range(k+1):    #n= number.index(max(number[0:k+1]))
            if number[i]==9:    #무작정 max보다는 9일때 빠르게 끝내는게 속도에 도움이됨
=======
        for i in range(k+1):
            if number[i]==9:
>>>>>>> f8ecbfbb71dce70d51645c3296da1d1fecdc9f95
                n=i
                break
            elif number[i]>number[n]:
                n=i
<<<<<<< HEAD

        for i in range(n):      #number=number[n:]
            number.popleft()    #O(1)로O(n)인리스트 복사보다 빠름
=======
        #n= number.index(max(number[0:k+1]))
        #number=number[n:]
        for i in range(n):
            number.popleft()
>>>>>>> f8ecbfbb71dce70d51645c3296da1d1fecdc9f95
            length-=1
        answer+=str(number.popleft())
        length-=1
        k-=n
    if len(number)==k:
        return answer
    else:
        for i in number:
            answer+=str(i)
<<<<<<< HEAD
    return answer

print(solution('21',1))
=======
    return answer
>>>>>>> f8ecbfbb71dce70d51645c3296da1d1fecdc9f95
