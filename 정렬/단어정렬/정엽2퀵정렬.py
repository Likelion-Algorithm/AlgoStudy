def quick(unsorted):
    if len(unsorted) <= 1:
        return unsorted
    pivot = unsorted[-1]
    max_list, min_list, same = [], [], []
    for i in unsorted:
        if len(pivot) > len(i):
            min_list.append(i)
        elif len(pivot) < len(i):
            max_list.append(i)
        else:
            if pivot > i:
                min_list.append(i)
            elif pivot < i:
                max_list.append(i)
            else:
                same.append(pivot)

    return(quick(min_list) + same + quick(max_list))

import sys
n = int(sys.stdin.readline().strip())
set1 = set(sys.stdin.readline().strip() for i in range(n))
list1 = list(set1)
for i in quick(list1):
    print(i)