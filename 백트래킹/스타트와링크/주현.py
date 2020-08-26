import sys
from itertools import combinations
num = int(sys.stdin.readline())
people = set()
team = []
status = []
value = []
for i in range(num):
    people.add(i)
    status.append(list(map(int, sys.stdin.readline().split())))
team = list(combinations(people,num//2))
for i in range(len(team)):         # 가능한 한 팀의 조합(nCn/2)을 set자료형으로 리스트에 담는다
    team[i] = set(team[i])
def evalueation(ateam, bteam):     #두 팀간 전력차를 반환하는 함수.
    ateam = list(ateam)
    bteam = list(bteam)
    avalue = 0
    bvalue = 0
    for i in ateam:
        for j in ateam:
            if i!=j:
                avalue+=status[i][j]
    for i in bteam:
        for j in bteam:
            if i!=j:
                bvalue+=status[i][j]
    return abs(avalue-bvalue)
while team:                       #한 팀을 추출해서 차집합 하면 상대팀을 만들 수 있다.  
    ateam = team.pop()
    bteam = people-ateam
    value.append(evalueation(ateam,bteam))
    team.remove(bteam)

print(min(value))                  #팀 전력을 최소화 한 값 출력
