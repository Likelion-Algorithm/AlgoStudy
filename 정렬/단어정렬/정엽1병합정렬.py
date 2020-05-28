import sys


def merge_sort(words):
    if len(words) == 1:
        return(words)
    mid = len(words)//2
    return merge(merge_sort(words[:mid]),merge_sort(words[mid:]))


def merge(smallnum, bignum):
    i = 0
    j = 0
    temp = []
    while(len(smallnum)>i) & (len(bignum)>j):
        if len(smallnum[i]) < len(bignum[j]):
            temp.append(smallnum[i])
            i+=1
        elif len(smallnum[i]) == len(bignum[j]):
            if smallnum[i]<bignum[j]:
                temp.append(smallnum[i])
                i+=1
            else:
                temp.append(bignum[j])
                j+=1
        else:
            temp.append(bignum[j])
            j+=1
    while(len(smallnum)>i):
        temp.append(smallnum[i])
        i+=1

    while(len(bignum)>j):
        temp.append(bignum[j])
        j+=1
    return temp

n = int(input())
set1 = set(sys.stdin.readline().strip() for i in range(n))
list1 = list(set1)
for i in merge_sort(list1):
    print(i)





