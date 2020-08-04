N = int(input())
timelist = list()
count = 1
for i in range(N):
    a,b = input().split()
    a,b = int(a),int(b)
    timelist.append([a,b])

timelist = sorted(timelist, key=lambda x:(x[1],x[0]))
temp = timelist[0][1]
for i in range(1,len(timelist)):
    if(timelist[i][0]>=temp):
        count+=1
        temp = timelist[i][1]
print(count)