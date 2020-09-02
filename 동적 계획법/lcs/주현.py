first = input()
second = input()
dpList = [[0 for col in range(len(first)+1)] for row in range(len(second)+1)]
for i in range(1,len(first)+1):
    for j in range(1,len(second)+1):
        if first[i-1]==second[j-1] :
            dpList[i][j]=dpList[i-1][j-1]+1
        else:
            dpList[i][j]= max(dpList[i-1][j],dpList[i][j-1])        
print(dpList[-1][-1])