num = int(input())
numList = list(map(int,input().split()))
opList = list(map(int,input().split()))
functionList = []
combination = []   
def opAssemble(combination,opList):
    if len(combination)==num-1:                     #연산자의 수가 num이 되면 순서대로 계산한다.
        count = numList[0]
        for i in range(len(combination)):
            if combination[i]==1:
                count+=numList[i+1]
            elif combination[i] ==2:
                count-=numList[i+1]
            elif combination[i] ==3:
                count*=numList[i+1]
            elif combination[i] ==4:
                count =div(count,numList[i+1])
        functionList.append(count)
        return

        
    else:
        for i in range(4):                          #가능한 연산자를 모두 조합하여 재귀한다.
            tempcombination = combination[::]
            tempOp = opList[::]
            if i == 0 and  opList[i]!=0:
                tempOp[i]-=1
                tempcombination.append(1)
                opAssemble(tempcombination,tempOp)
            if i == 1 and  opList[i]!=0:
                tempOp[i]-=1
                tempcombination.append(2)
                opAssemble(tempcombination,tempOp)
            if i == 2 and  opList[i]!=0:
                tempOp[i]-=1
                tempcombination.append(3)
                opAssemble(tempcombination,tempOp)
            if i == 3 and  opList[i]!=0:
                tempOp[i]-=1
                tempcombination.append(4)
                opAssemble(tempcombination,tempOp)
def div(a,b):
    if a<0 or b<0:
        return -(abs(a)//abs(b))
    else:
        return a//b
opAssemble(combination,opList)
print(max(functionList))
print(min(functionList))        #가능한 조합의 최대와 최소를 출력
''' 시간초과에 걸리지 않았지만 이런 조합문제가 나오면 combinations메소드를 떠올려야
    할 것 같다.'''