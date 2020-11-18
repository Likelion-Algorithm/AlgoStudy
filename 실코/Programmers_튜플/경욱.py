def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s = sorted(s, key = lambda x : len(x) )
    for i in range(len(s)):
        c = s[i].split(',')
        for j in range(len(c)):
            if int(c[j]) not in answer:
                answer.append(int(c[j]))
    return answer