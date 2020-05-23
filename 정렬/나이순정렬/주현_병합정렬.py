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
        if(list[i][0]<list[j][0]):
            templist.append(list[i])
            i+=1
        elif(list[i][0]>list[j][0]):
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

num = int(input())
userlist=[]
for i in range(num):
    userlist.append(input().split())
    userlist[i][0]=int(userlist[i][0])
        
split(0,num-1,userlist)
for i in range(num):
    print(userlist[i][0], userlist[i][1])

''' 퀵 정렬의 고유한 특성 때문에 사실상 퀵정렬로 구현하는 것이 어려운 문제다. 
    물론 병합 정렬도 완벽하게 짜여있지 않을 경우 틀릴 가능성이 있다. 
    하지만 제대로 짜여진 병합정렬은 같은 크기의 자료가 이동하지 않는데, 
    이는 특정한 상황에서 메모리를 감수하고도
    필수적으로 사용해야 할 이유가 된다.'''
