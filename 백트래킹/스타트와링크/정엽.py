def calculate(aTeam):
    bTeam = list(numSet-set(aTeam))
    cntA, cntB = 0,0
    for i in aTeam:
        for j in aTeam:
            cntA += graph[i-1][j-1]
    for i in bTeam:
        for j in bTeam:
            cntB += graph[i-1][j-1]
    return abs(cntA-cntB)


def find(verification, playerList, selectedList):
    global cnt
    if len(selectedList) == verification:
        cnt-=1
        return calculate(selectedList)
    minimum = float('inf')
    for i in playerList:
        if cnt <= 0:
            return minimum
        temp = find(verification,numList[i:],selectedList+[i])
        minimum = min(minimum,temp)
    return minimum
import sys
from math import factorial

n = int(sys.stdin.readline().strip())
graph = [list(map(int,sys.stdin.readline().split())) for i in range(n)]

verify = n//2
numSet = set(i for i in range(1,n+1))
numList = [i for i in range(1,n+1)]

cnt = int(factorial(n)/(factorial(verify)*factorial(n-verify)))//2

print(find(verify,numList, []))

