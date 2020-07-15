import sys
time = []
for i in range(int(sys.stdin.readline().strip())):
    a = list(map(int,sys.stdin.readline().split()))
    time.append(a)
time = sorted(time, key=lambda x: (x[1],x[0]))
now = time[0][1]
cnt = 1
i = 1
while i < len(time):
    if now<=time[i][0]:
        now = time[i][1]
        cnt += 1
        i+=1
    else:
        i+=1
print(cnt)





