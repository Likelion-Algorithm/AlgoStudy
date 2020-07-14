n = int(input())
fiboList = list()
fiboList.append(0)
fiboList.append(1)
if n>=2:
    for i in range(2,n+1):
        fiboList.insert(i,fiboList[i-1]+fiboList[i-2])

print(fiboList[n])