def solution(citations):
    answer = 0
    citations.sort()
    n=len(citations)
    m=max(citations)
    for i in range(m+1):
        for j in range(n):
            if citations[j]>=i and n-j>=i:
                if i>answer:
                    answer=i
                break
    return answer