def quickSort(a,b, list):
    if(b-a<2):
        return
    l=a
    r=b
    pivot=a
    for i in range(a,b):
        l=i
        if len(list[l])>len(list[pivot]):
            break
    for j in range(b-1,a-1,-1):
        r=j
        if len(list[r])<len(list[pivot]):
            break
    if l<r:
        swap(l,r,list)
        quickSort(a,b,list)
    else:
        swap(r,pivot,list)
        quickSort(a,r,list)
        quickSort(l,b,list)

def swap(a,b,list):
    temp=list[a]
    list[a]=list[b]
    list[b]=temp

num = int(input())
list = []
for i in range(0,num):
    list.append(input())

quickSort(0,num,list)

for l in range(0, len(list)) :
    if(list[l]==list[l-1]):
        if(l==0):
            print(list[l])
        continue
    print(list[l])

'''백준에서 런타임에러 발생'''