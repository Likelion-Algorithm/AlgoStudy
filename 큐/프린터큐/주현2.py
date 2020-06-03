class PrintQueue:
    def __init__(self,docQty,docLoc,importance):
        self.docQty = docQty
        self.docLoc = docLoc
        self.importance = importance
        self.order=0
        self.front=0
        self.rear=len(self.importance)
        

    def getOrder(self):
        i=self.front
            while(self.importance[i]<self.importance[self.front]):
                i+=1
                if(i==self.rear):
                    self.deQueue()
            self.enQueue(self.deQueue())

    def deQueue(self):
        temp=self.importance[self.front]
        self.importance[self.front]=0
        self.front+=1
        return temp
        
    def enQueue(self,data):
        self.importance.append(data)
        self.rear+=1

    
testcase = int(input())
classLi = []
for i in range(0,testcase):
    docQty, docLoc = map(int, input().split())
    importance = list(map(int, input().split()))
    printqueue = PrintQueue(docQty,docLoc,importance)
    classLi.append(printqueue)
for j in range(0,testcase):
    print(classLi[j].getOrder())