def solution(n, results):
    answer = 0
    W, L= [set() for _ in range(n+1)], [set() for _ in range(n+1)]
    
    for i in range(1, n+1):
        for result in results:
            winner, loser = result[0], result[1]
            if i == winner:
                W[i].add(loser)
            if i == loser:
                L[i].add(winner)
        for winner in L[i]: # i를 이긴 사람은 i가 이긴 사람들을 다 이길 수 있다.
            W[winner].update(W[i])
        for loser in W[i]: # i에게 진 사람은 i를 이긴 사람들을 못이긴다.
            L[loser].update(L[i])
                
    for i in range(1, n+1):
        if len(W[i]) + len(L[i]) == n - 1:
            answer += 1
            
    return answer
