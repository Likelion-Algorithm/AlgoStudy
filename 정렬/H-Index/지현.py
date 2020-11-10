def solution(citations):

    answer = []
    citations = sorted(citations)
    h = 0

    while True:
        
        cnt = 0

        for i in citations:
            if i >= h:
                cnt += 1
            else:
                pass

        if cnt >= h:
            answer.append(h)
            h+= 1
        else:
            return answer[-1]

print(solution([10, 9, 4, 1, 1]))

#시간초과 뜰 줄 알았는데 안떳당..왜지..암튼통과
        