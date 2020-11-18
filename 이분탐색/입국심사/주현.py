def solution(n, times):
    심사 = [0]*len(times)
    start = 0
    end = n*min(times)
    answer = end
    while end>=start :
        mid = (end+start)//2
        for i in range(len(times)):
            심사[i] = mid//times[i]
        if sum(심사)>n:
            if mid < answer:
                answer = mid
            end=mid-1
        elif sum(심사)==n:
            if mid < answer:
                answer = mid
            end=mid-1
        else:
            start=mid+1
    return answer

print(solution(6, [4,10]))