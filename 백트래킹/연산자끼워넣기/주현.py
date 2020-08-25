num = int(input())
numList = list(map(int,input().split()))
opList = list(map(int,input().split()))
functionList = []
queue = []   
def opAssemble(queue,opList):
    if len(queue)==num-1:
        count = numList[0]
        for i in range(len(queue)):
            if queue[i]==1:
                count+=numList[i+1]
            elif queue[i] ==2:
                count-=numList[i+1]
            elif queue[i] ==3:
                count*=numList[i+1]
            elif queue[i] ==4:
                count = div(count,numList[i+1])
        functionList.append(count)
        return

        
    else:
        for i in range(4):
            tempQueue = queue[::]
            tempOp = opList[::]
            if i == 0 and  opList[i]!=0:
                tempOp[i]-=1
                tempQueue.append(1)
                opAssemble(tempQueue,tempOp)
            if i == 1 and  opList[i]!=0:
                tempOp[i]-=1
                tempQueue.append(2)
                opAssemble(tempQueue,tempOp)
            if i == 2 and  opList[i]!=0:
                tempOp[i]-=1
                tempQueue.append(3)
                opAssemble(tempQueue,tempOp)
            if i == 3 and  opList[i]!=0:
                tempOp[i]-=1
                tempQueue.append(4)
                opAssemble(tempQueue,tempOp)
def div(a,b):
    if a<0 or b<0:
        return -(abs(a)//abs(b))
    else:
        return a//b
opAssemble(queue,opList)
print(max(functionList))
print(min(functionList))