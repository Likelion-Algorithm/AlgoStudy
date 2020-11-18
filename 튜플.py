def solution(s):
    answer = []
    a= s.split(",")
    temp = list()
    b = ''
    for i in a:
        # if not '{' in i and not'}' in i and not'{{' in i and not'}}' in i:
        for j in i:
            if j != '{':
                if j == '}':
                    temp.append(b)
                    b=''
                else:
                    b += j
    return answer