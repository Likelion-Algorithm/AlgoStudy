def solution(n, times):
    answer = 0
    last = min(times)
    time = 0
    cnt = n-2
    a = times.pop(0)
    while cnt:
        if time == a:
            cnt -= 1
            times.append(2*a)
            a = times.pop(0)
        time +=1
    time += last
    answer = time
    return answer