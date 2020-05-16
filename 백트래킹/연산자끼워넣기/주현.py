num = int(input())
numList = list(map(int,input()))
operator = list(map(int,input()))
oplist=[[],[],[],[]]
for i in operator:
    for j in range(0,i):
        if(i==operator[0]):
            oplist.append('sum')
        elif(i==operator[1]):
            oplist.append('sub')
        elif(i==operator[2]):
            oplist.append('mul')
        elif(i==operator[3]):
            oplist.append('div')

//못하겠다

