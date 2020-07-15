def quick_sort(num):
    if len(num)<=1:
        return num
    pivot = num[-1]
    less, greater, equal = [], [], []
    for i in num:
        if i < pivot:
            less.append(i)
        elif i>pivot:
            greater.append(i)
        else:
            equal.append(i)
    return quick_sort(less)+equal+quick_sort(greater)

import sys
sys.stdin.readline()
list1 = quick_sort(list(map(int,sys.stdin.readline().split())))
summation, answer = 0,0
for i in list1:
    summation+=i
    answer+=summation
print(answer)