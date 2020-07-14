import sys
n,k = map(int, sys.stdin.readline().split())
valueList = list()
valueList.append(0)
for i in range(n):
    valueList.append(int(sys.stdin.readline()))
answerList = list()
for i in range(k+1):
    answerList.append(0)
answerList[0]=1
for i in range(1,len(valueList)):      #동전의 가치 탐색(1번째 동전만, 1,2번째 동전만, 1,2,3번째....)                                     
    for j in range(1,k+1):             #문제의 크기 탐색
        if j>=valueList[i]:
            answerList[j]= answerList[j-valueList[i]] + answerList[j]  #점화식->
    
print(answerList[-1])

        
        