from collections import deque
from itertools import islice
def solution(priorities, location):
    answer = 0
    priorities[location] = float(priorities[location])
    priorities = deque(priorities)
    while priorities:
        num = priorities.popleft()
        if priorities:
            if num >= max(priorities):
                answer+=1
                if type(num) == float:
                    return answer
            else:
                priorities.append(num)
        else:
            answer+=1
    return answer