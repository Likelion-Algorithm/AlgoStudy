import sys
from collections import OrderedDict

def quick_sort(data_list):
    if len(data_list)<=1:
        return data_list
    left,right = list(),  list()
    pivot = data_list[0]
    # 피봇 설정
    for index in range(1,len(data_list)):
        # 길이에 따른 분류
        if pivot > data_list[index]:
            # 피봇이 큰경우 왼쪽에
            left.append(data_list[index])
        else: 
                # 피봇이 작은 경우 오른쪽에
            right.append(data_list[index])
    return quick_sort(left) + [data_list[0]] + quick_sort(right)
def getMost(nlist,num):
    nlistset =list(OrderedDict.fromkeys(nlist))
    most = {}
    keylist = list()
    for i in range(len(nlistset)):
        most[nlistset[i]]=nlist.count(nlistset[i])
    templist = list(OrderedDict.fromkeys(most.values()))
    for key , value in most.items():
        if value==templist[-1]:
            keylist.append(key)
    if(len(keylist)>=2):
        return keylist[1]
    else:
        return keylist[0]

num = int(sys.stdin.readline())
nlist = list()
for i in range(num):
    nlist.append(int(sys.stdin.readline()))
average = sum(nlist)//num
print(average)
nlist = quick_sort(nlist)
print(nlist[num//2])
print(getMost(nlist,num))
print(nlist[-1]-nlist[0])