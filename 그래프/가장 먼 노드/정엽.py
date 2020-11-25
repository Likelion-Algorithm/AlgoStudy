from collections import defaultdict, deque
def solution(n,edge):
    dict1, list1 = defaultdict(list),[float('inf')]*n
    list1[0], list2 = 0, deque([1])
    for x,y in edge:
        dict1[x].append(y)
        dict1[y].append(x)
    while True:
        if not list2:
            break
        x = list2.popleft()
        for i in dict1[x]:
            if list1[i-1] > list1[x-1] + 1:
                list1[i-1] = list1[x-1] +1
                list2.append(i)
    return list1.count(max(list1))
