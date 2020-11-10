from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        person = people.pop()
        if people:
            동승=people.popleft()
            if 동승<=limit-person:
                answer+=1
            else:
                people.appendleft(동승)
                answer+=1
        else:
            answer+=1
    return answer