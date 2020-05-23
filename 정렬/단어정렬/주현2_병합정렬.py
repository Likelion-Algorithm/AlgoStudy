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
        if(len(list[i])<len(list[j])):
            templist.append(list[i])
            i+=1
        elif(len(list[i])>len(list[j])):
            templist.append(list[j])
            j+=1
        else:
            if(list[i]<list[j]):
                templist.append(list[i])
                i+=1
            elif(list[i]>list[j]):
                templist.append(list[j])
                j+=1
            else:
                templist.append(list[i])
                templist.append(list[j])
                i+=1
                j+=1
    if(i==a+((b-a)//2)+1):
        while(j!=b+1):
            templist.append(list[j])
            j+=1
    else:
        while(i!=a+((b-a)//2)+1):
            templist.append(list[i])
            i+=1
    list[a:b+1]=templist[:]
            
num = int(input())
list = []
for i in range(0,num):
    list.append(input())

split(0,num-1,list)

for l in range(0, len(list)) :
    if(list[l]==list[l-1]):
        if(l==0):
            print(list[l])
        continue
    print(list[l])

'''정렬은 가능하지만 병합정렬의 본질과 동떨어진 코드다. 더 짧게 만들 수 있음에도
   불필요한 동작이 많아 병합정렬임에도 같은 순위의 자료가 이동한다.'''
