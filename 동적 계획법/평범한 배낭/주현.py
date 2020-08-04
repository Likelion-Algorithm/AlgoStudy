num, maxweight = map(int,input().split())
wvList = []
for i in range(num+1):
    if i==0:
        wvList.append([0,0])
    else:
        a,b = map(int,input().split())
        wvList.append([a,b])
dpList = [[0 for col in range(maxweight+1)] for row in range(num+1)]

for i in range(1,num+1):
    for j in range(1,maxweight+1):
        if j>=wvList[i][0]:
            if (dpList[i-1][j-wvList[i][0]]+wvList[i][1]> dpList[i-1][j]):
                dpList[i][j]=dpList[i-1][j-wvList[i][0]]+wvList[i][1]
            else:
                dpList[i][j]=dpList[i-1][j]
        else:
            dpList[i][j]=dpList[i-1][j]

print(dpList[-1][-1])