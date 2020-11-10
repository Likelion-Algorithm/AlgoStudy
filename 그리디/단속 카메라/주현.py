def solution(routes):
    answer = 0
    loc=[]
    routes.sort(reverse=True)
    while routes:
        minRoutes = routes.pop()
        if not loc:
            loc = [minRoutes[0],minRoutes[1]]
        else:
            loc[0] = minRoutes[0]
            loc[1] = minRoutes[1] if minRoutes[1]<loc[1] else loc[1]
        if routes and routes[-1][0]<=loc[1]:
            continue
        else:
            answer+=1
            loc = []
<<<<<<< HEAD
    return answer
=======
    return answer
    
'''그리디 문제에서 어느 부분을 그리디하게 뽑을 것인지 다양하게 생각해야 한다.
   루트의 길이에 꽂혀서 정렬 부분을 key = lambda x:x[1]-x[0]으로 하고, 거기에 맞춰서 했다가
   하루종일 풀 수 없었다. 
   각 routes의 첫 원소, 즉 routes의 시작점을 기준으로 그리디하게 뽑으면 쉽게 해결할 수 있다.'''

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))
>>>>>>> 821aa35... 그리디 수정
