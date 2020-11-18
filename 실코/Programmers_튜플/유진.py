def solution(s):
    ans = list()
    temp = list()
    for x in s.split('},'):
        temp.append(x.replace('{{','').replace('{','').replace('}}',''))
    temp = sorted(temp, key=lambda x: len(x))
    for i in temp:
        t2 = [int(x) for x in i.split(',')]
        for x in t2:
            if x not in ans:
                ans.append(x)
    return ans
