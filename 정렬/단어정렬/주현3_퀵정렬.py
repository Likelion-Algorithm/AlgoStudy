def quickSort(a,b, list):
    left=a
    right=b
    pivot=a
    while(left<right):
        for left in range(a, b+1):
            if(len(list[left])>len(list[pivot])):
                break
            elif(len(list[left])==len(list[pivot])):
                if(list[left]>list[pivot]):
                    break
        for right in range(b, a-1, -1):
            if(len(list[right])<len(list[pivot])):
                break
            elif(len(list[right])==len(list[pivot])):
                if(list[right]<list[pivot]):
                    break
        if(left<right):
            swap(left,right,list)
    if(a<b):
        swap(right,pivot,list)
        pivot=right
        quickSort(a,pivot-1,list)
        quickSort(pivot+1,b,list)



def swap(a,b,list):
    temp=list[a]
    list[a]=list[b]
    list[b]=temp

num = int(input())
list = []
for i in range(0,num):
    list.append(input())

quickSort(0,num-1,list)

for l in range(0, len(list)) :
    if(list[l]==list[l-1]):
        if(l==0):
            print(list[l])
        continue
    print(list[l])

'''백준에서 시간초과 발생'''