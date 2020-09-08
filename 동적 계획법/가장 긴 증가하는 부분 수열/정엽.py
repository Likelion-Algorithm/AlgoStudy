import sys
n,numList = int(sys.stdin.readline()),list(map(int,sys.stdin.readline().split()))
answerList = [1]*len(numList)
for i in range(n):
    for j in range(i+1,n):
        if numList[i]<numList[j]:answerList[j]=max(answerList[j],answerList[i]+1)
print(max(answerList))