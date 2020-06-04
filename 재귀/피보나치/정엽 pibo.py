def pibo(first,second,num_list):
    if len(num_list) == n+1:
        print(num_list[-1])
        return
    num_list.append(first+second)
    return(pibo(num_list[-1],num_list[-2],num_list))

import sys
n = int(sys.stdin.readline().strip())
list1 = [0,1]
if n<2:
    print(list1[n])
else:
    pibo(list1[-1],list1[-2],list1)


