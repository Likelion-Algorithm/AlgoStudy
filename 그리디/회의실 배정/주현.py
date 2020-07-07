N = int(input())
timelist = list()
timesub = list()
rangelist = set()
count = 0
temp = 1
tempmax = 0
tempmin = 0
for i in range(N):
    a,b = input().split()
    a,b = int(a),int(b)
    if a < tempmin:
        tempmin = a
    if b > tempmax:
        tempmax = b
    timelist.append((a,b))
    timesub.append(b-a)
while (tempmax-tempmin)-len(rangelist)>min(timesub): #timesub시 시간초과
    loc = timesub.index(min(timesub))
    if (timelist[loc][1]-1 not in rangelist and timelist[loc][0]+1 not in rangelist):
        i = range(timelist[loc][0],timelist[loc][1]+1)
        rangelist.update(list(i))
        count+=1
    timelist.pop(loc)
    timesub.pop(loc)

print(count)

    