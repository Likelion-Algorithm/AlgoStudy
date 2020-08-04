class PrintQueue:
    def __init__(self,docQty,docLoc,importance):
        self.docQty = docQty
        self.docLoc = docLoc
        self.importance = importance
        self.order=0
        self.front=0
        self.rear=len(self.importance)
        

    def getOrder(self):
        while 1 :
            while self.importance[self.front]!=max(self.importance):
                for i in range(self.front+1,self.rear):
                    if(self.importance[self.front]<=self.importance[i]):
                        if(self.front==self.docLoc):
                            self.docLoc=self.rear
                        self.enQueue(self.deQueue())
                        break
            self.deQueue()
            self.order+=1
            if(self.front-1==self.docLoc):
                return self.order

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

'''같은 기능을 하는데, 값만 다른 큐와 함수가 testcase 만큼의 수로 들어오기에
class를 통해 인스턴스를 만들 것을 쉽게 계획할 수 있었다. 로직을 구현하는데 급급했기에,
전반적인 코드의 길이나 변수명은 깔끔하지 못했고, front와 rear를 사용하지 않고는
푸는 것이 거의 불가능하다고 느꼈다.(docLoc때문에)자동으로 index를 정리해주는
리스트 함수를 맹신할 수는 없을 것같다.'''