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
    return answer