num = int(input())
stairList = list()
maxList = list()
stairList.append(0)
for i in range(1,num+1):
    stairList.append(int(input()))
maxList.append([0,0])
maxList.append([0,stairList[1]])

for i in range(2,num+1):
    if(maxList[i-2][1]>maxList[i-1][1] or (maxList[i-2][1]<=maxList[i-1][1] and maxList[i-1][0]==1 )):
        maxList.append([2,(maxList[i-2][1]+stairList[i])]) 
    else:
        maxList.append([1,(maxList[i-1][1]+stairList[i])]) 

print(maxList[-1][1])