num = int(input())
list = []
for i in range(0,num):
    list.append(input())
for j in range(0,num-1):
    for k in range(j+1,num):
        if(len(list[j])>len(list[k])):
            a=list[j]
            list[j]=list[k]
            list[k]=a
        elif(len(list[j])==len(list[k])):
            if(list[j]>list[k]):
                a=list[j]
                list[j]=list[k]
                list[k]=a
for l in range(0, len(list)) :
    if(list[l]==list[l-1]):
        if(l==0):
            print(list[l]) 
        continue
    print(list[l])

'''직관적이지만 실전에서는 시관초과로 사용이 불가하다.(백준 불통과 코드)'''
    