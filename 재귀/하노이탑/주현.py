              
num = int(input())
movelist = list()
templist = list()
for i in range(6):
    movelist.append([i])
    templist.append([])

for i in range(1,num):
    for j in range(6):
        if j==0 or j==1:
            templist[j]= movelist[(j+1)%2]+[j]+movelist[5-(j*2)]
        elif j==2 or j==3:
            templist[j]= movelist[2+(j+1)%2]+[j]+movelist[10%(j*3)]
        else:
            templist[j]= movelist[4+(j+1)%2]+[j]+movelist[10%(j*2)]
    movelist=templist[:]

print(len(movelist[1]))
for i in range(len(movelist[1])):
    if movelist[1][i]==0:
        print('1','2')
    elif movelist[1][i]==1:
        print('1','3')
    elif movelist[1][i]==2:
        print('2','1')
    elif movelist[1][i]==3:
        print('2','3')
    elif movelist[1][i]==4:
        print('3','1')
    elif movelist[1][i]==5:
        print('3','2')

#동적계획법 만세
#푸는데 2주걸림