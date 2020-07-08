def merge_sort(stats):
    if len(stats) <= 1:
        return stats
    mid = len(stats)//2
    return merge(merge_sort(stats[:mid]), merge_sort(stats[mid:]))

def merge(left, right):
    i = 0
    j = 0
    temp = []
    while (i<len(left)) & (j<len(right)):
        if left[i] > right[j]:
            temp.append(right[j])
            j += 1
        elif left[i] == right[j]:
            temp.append(left[i])
            temp.append(right[j])
            i+=1
            j+=1
        else:
            temp.append(left[i])
            i+=1

    while (i<len(left)):
        temp.append(left[i])
        i+=1

    while (j<len(right)):
        temp.append(right[j])
        j+=1

    return temp

# def mode(stats):
#     set1 = set(stats)
#     dict1 = {}
#     maximum = 0
#     for i in list(set1):
#         n = stats.count(i)
#         if n>maximum:
#             maximum = n
#         if n not in dict1:
#             dict1[n] = [i]
#         else:
#             dict1[n].append(i)
#     if len(dict1[maximum])<2:
#         print(dict1[maximum][0])
#     else:
#         print(merge_sort(dict1[maximum])[1])

def mode(stats):
    from collections import Counter
    a = Counter(stats)
    a = sorted(a.most_common(), key = lambda x:(-x[1], x[0]))
    if len(a)>=2:
        print(a[1][0] if a[0][1] == a[1][1] else a[0][0])
    else:
        print(a[0][0])

import sys
num = [int(sys.stdin.readline()) for i in range(int(sys.stdin.readline().strip()))]
sort_stat = merge_sort(num)
print(round((sum(sort_stat))/(len(sort_stat))))
print(sort_stat[len(sort_stat)//2])
mode(sort_stat)
if len(sort_stat) == 1:
    print(0)
else:
    print(sort_stat[-1] - sort_stat[0])




