class PrintQueue:

    def __init__(self,docQty,docLoc,importance):
        self.docQty = docQty
        self.docLoc = docLoc
        self.importance = importance
        

    def getOrder(self):
        order=1
        while(self.importance[0] != self.importance[self.docLoc]):
            for i in range(0, len(self.importance)):
                if(self.importance[0]<self.importance[i]):
                    self.enQueue(self.deQueue())
        
            self.deQueue()
            order += 1
        return order

    def deQueue(self):
        if self.importance[self.docLoc]!=self.importance[0]:
            self.docLoc-=1
        return self.importance.pop(0)
        
    def enQueue(self,data):
        self.importance.append(data)
        if data==self.importance[self.docLoc]:
            self.docLoc=len(self.importance)-1

    
testcase = int(input())
classLi = []
for i in range(0,testcase):
    docQty, docLoc = map(int, input().split())
    importance = list(map(int, input().split()))
    printqueue = PrintQueue(docQty,docLoc,importance)
    classLi.append(printqueue)
for j in range(0,testcase):
    print(classLi[j].getOrder())