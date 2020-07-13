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
for i in range(1,len(valueList)):
    for j in range(1,k+1):
        if j>=valueList[i]:
            answerList[j]= answerList[j-valueList[i]] + answerList[j]
    
print(answerList[-1])

        
        