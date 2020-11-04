def solution(name):
    answer = 0
    loc = 0
    length = len(name)
    check = []
    for i in range(length):
        if name[i] =='A':
            check.append(i)
    
    while len(check) != length:
        front = loc
        back = loc
        fmove = 0
        bmove = 0            
        while front in check:
            front+=1
            fmove+=1
            if front>length-1:
                front = 0
        while back in check:
            back-=1
            bmove+=1
            if back<0:
                back = length-1
        if fmove<=bmove:
            answer += fmove
            answer = answer + 91 - ord(name[front]) if name[front]>'N' else answer + ord(name[front]) - 65
            loc = front
            check.append(front)
        else:
            answer += bmove
            answer = answer + 91 - ord(name[back]) if name[back]>'N' else  answer + ord(name[back]) - 65
            loc = back
            check.append(back)


    return answer