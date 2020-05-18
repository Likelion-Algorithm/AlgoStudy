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
            if(list[i][1]<list[j][1]):
                templist.append(list[i])
                i+=1
            elif(list[i][1]>list[j][1]):
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

num = int(input())                       # 좌표의 개수를 받는다.
loclist=[]
for i in range(0,num):
    a,b=input().split()
    loclist.append([int(a),int(b)])      # 2차원 배열에 좌표를 저장한다.

split(0,num-1,loclist)                   # mergesort 실행

for j in range(0,num):
    print(loclist[j][0],loclist[j][1])   #출력



