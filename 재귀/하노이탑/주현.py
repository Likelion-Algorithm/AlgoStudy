def getCount(Base, count, num, Baselist):
    while len(hanoiBase3)!=num:
        tempmax=0
        tempmin=0
        for i in range(0,3):
            if i==Base:
                continue
            if Baselist[i][-1]>Baselist[tempmax][-1]:
                tempmax=i
        for j in range(0,3):
            if j==tempmax or Baselist[j][-1]>Baselist[tempmax][-1]:
                continue
            if Baselist[j][-1]<=Baselist[tempmin][-1]:
                tempmin=j
        if Baselist[tempmin][-1]==0:
            Baselist[tempmin].append(Baselist[tempmax].pop())
            Base=tempmin
            count+=1
            continue
        elif(Baselist[tempmax][-1]==max(Baselist[0][-1],Baselist[1][-1],Baselist[2][-1])):
            for k in range(0,3):
                if(k!=tempmax and k!=Base):
                    tempmax=k
                    if tempmin==tempmax:
                        tempmin=(tempmin+1)%2
                    break
            for j in range(0,3):
                if j==tempmax or Baselist[j][-1]<Baselist[tempmax][-1]:
                    continue
                else:
                    tempmin=j
        Baselist[tempmin].append(Baselist[tempmax].pop())
        Base=tempmin
        count+=1
        continue

    Baselist[2].append(Baselist[0].pop())
    count+=1
    return count

num = int(input())
hanoiBase1=list()
hanoiBase2=list()
hanoiBase3=list()
hanoiBase1.append(0)
hanoiBase2.append(0)
hanoiBase3.append(0)
Baselist=[hanoiBase1,hanoiBase2,hanoiBase3]
count=0
Base=3
for block in range(num,0,-1):   #첫 번째 장대에 세팅
    hanoiBase1.append(block)
print(getCount(Base,count,num,Baselist))
    