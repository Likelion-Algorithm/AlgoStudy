import sys
from collections import Counter
def split(i,j,list):
    if(j-i+1>=2):
        split(i,(i+j)//2,list)
        split((i+j)//2+1,j,list)
        merge(i,j,list)
        
def merge(a,b,list):
    i=a
    j=a+((b-a)//2)+1
    templist=[]
    while(i!=a+((b-a)//2)+1 and j!=b+1):
        if(list[i]<list[j]):
            templist.append(list[i])
            i+=1
        elif(list[i]>list[j]):
            templist.append(list[j])
            j+=1
        else:
            templist.append(list[i])
            i+=1

    if(i==a+((b-a)//2)+1):
        while(j!=b+1):
            templist.append(list[j])
            j+=1
    else:
        while(i!=a+((b-a)//2)+1):
            templist.append(list[i])
            i+=1
    list[a:b+1]=templist[:]
def getMost(nlist):
    most = Counter(nlist)
    most = most.most_common()
    if(len(most)>=2):
        if(most[0][1]==most[1][1]):
            return most[1][0]
    return most[0][0]
num = int(sys.stdin.readline())
nlist = list()
for i in range(num):
    nlist.append(int(sys.stdin.readline()))
average = sum(nlist)/num
print(round(average))
split(0,num-1,nlist)
print(nlist[num//2])
print(getMost(nlist))
print(nlist[-1]-nlist[0])

#