import sys
n,k = map(int, sys.stdin.readline().split())
valueList = list()
valueList.append(0)
for i in range(n):
    valueList.append(int(sys.stdin.readline()))
answerList = [[0 for col in range(k+1)] for row in range(n+1)]
for i in range(n+1):
    answerList[i][0]=1
for i in range(1,len(valueList)):
    for j in range(1,k+1):
        answerList[i][j]= answerList[i][j-valueList[i]] + answerList[i-1][j]
    
print(answerList[-1][-1])

        
        