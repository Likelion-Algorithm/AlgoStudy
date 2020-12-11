def solution(n, results): 
    # win - 이긴 사람 : 진 사람 / lose - 진 사람 : 이긴 사람 
    # set()을 이용해야 중복이 방지됨. 
    win = {x:set() for x in range(1, n+1)} 
    lose = {x:set() for x in range(1, n+1)}
    
    for winner, loser in results: 
        win[winner].add(loser) 
        lose[loser].add(winner) 
    # win {1: {2}, 2: {5}, 3: {2}, 4: {2, 3}, 5: set()}
    # lose {1: set(), 2: {1, 3, 4}, 3: {4}, 4: set(), 5: {2}}
    
    # i를 이긴 사람들은 i가 이긴 사람들 또한 이긴다. 
    for i in range(1, n+1): 
        for winner in lose[i]: 
            win[winner].update(win[i]) 
        for loser in win[i]: 
            lose[loser].update(lose[i]) 
        # win과 lose의 합이 n-1일 경우, 해당 사람의 순위를 알 수 있다. 

    answer = 0 
    
    for i in range(1, n+1): 
        if len(win[i]) + len(lose[i]) == n-1: 
            answer += 1 
    return answer