import sys

n = int(sys.stdin.readline())
graph = []
s = []
tmp = []
result = []

answer = []
answer_minus = []
zero = []


for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


def Team_score(a):
    
    if len(tmp) == 2:
        result.append(graph[tmp[0]-1][tmp[1]-1])
        return

    for i in range(len(a)):

        if len(tmp) == 0:
            tmp.append(a[i])
            Team_score(a)
            tmp.pop()
        else:
            if a[i] in tmp:
                continue
            tmp.append(a[i])
            Team_score(a)
            tmp.pop()
            
'''
def Team_score(a):
    for i in range(a[0], a[-1]):
        for j in range(i+1, a[-1]+1):
           
            result.append(graph[i-1][j-1])
            result.append(graph[j-1][i-1])
'''   


def Team_make():
    
    if len(s) == n:
        
        n1 = s[:(n//2)]
        n2 = s[(n//2):]

        Team_score(n1)
        global result
        global answer
        answer.append(sum(result))
        result = []
        

        Team_score(n2)
        answer.append(sum(result))
        result = []
        

        if answer[0]> answer[1]:
            global answer_minus
            
            minus = answer[0]-answer[1]
            if minus not in answer_minus:
                answer_minus.append(minus)
               
        else:
            
            minus = answer[1]-answer[0]
            if minus not in answer_minus:
                answer_minus.append(minus)
             
        answer = []
        return
    
    for i in range(1, n+1):
        if len(s) == 0:
            s.append(i)
            Team_make()
            s.pop()
            
        else:
            if i in s:
                continue
            s.append(i)
            Team_make()
            s.pop()

    
Team_make()

print(min(answer_minus))


