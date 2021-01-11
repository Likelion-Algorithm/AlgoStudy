from collections import deque

T = int(input())

def fly(n):
    sequence = 0
    index = 0
    while sequence<n:
        index += 1
        sequence += 2*index

    if sequence-n < index:
        return index*2
    else:
        return (index*2)-1


answer = []
for i in range(T):
    a, b = map(int,input().split())
    answer.append(fly(b-a))

for i in answer:
    print(i)

#12 3344 555 6 6 6  7 7 7 78888......
#12 3456 789101112 13141516
#수열 표현 난이도가 악랄하다