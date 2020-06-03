class PrintQueue:

    def __init__(self,docQty,docLoc,importance):
        self.docQty = docQty
        self.docLoc = docLoc
        self.importance = importance
        

    def getOrder(self):
        order=0
        front = 0
        rear = len(self.importance)-1
        while(self.importance[self.docLoc] in self.importance):
            for i in range(front, rear):
                if(self.importance[front]<self.importance[i]):
                    self.enQueue(self.deQueue(front,rear),front,rear)
                else:
                    self.deQueue(front,rear)
                    order += 1
        return order

    def deQueue(self,front,rear):
        front += 1
        return self.importance.pop(0)

    def enQueue(self,data,front,rear):
        rear += 1
        self.importance.append(data)

    
testcase = int(input())
classLi = []
for i in range(0,testcase):
    docQty, docLoc = map(int, input().split())
    importance = list(map(int, input().split()))
    classLi.append(PrintQueue(docQty,docLoc,importance))

for j in range(0,testcase):
    print(classLi[j].getOrder())