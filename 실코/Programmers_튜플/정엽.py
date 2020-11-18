def solution(s):
    list1 = []

    a = ''.join(s.split('{')).split('}')
    for i in a:
        a = i.replace(',',' ')
        if not a:
            continue
        list1.append(a.split())
    list1 = list(map(set,list1))
    list1.sort()

    answer = []
    past =set()
    for i in range(len(list1)):
        answer.append(int(list(list1[i] - past)[0]))
        past = list1[i]
    return answer