n = int(input())

s = []
plus = []
minus = []
answer = 0

def Queen():
    
    if len(s) == n:
        global answer
        answer += 1
        return 
        
    for i in range(1, n+1):

        if len(s) != 0: 
            previous = s[-1]
            if i == previous-1 or i == previous+1 or i in s:
                continue

        s.append(i)

        a = (len(s)-1) + (i-1)
        b = (len(s)-1) - (i-1)

        if a in plus or b in minus:
            s.pop()
            continue
        else:
            plus.append(a)
            minus.append(b)
        
        Queen()
        s.pop()
        plus.pop()
        minus.pop()
     
Queen()
print(answer)