def merge_sort(str):

    if len(str)<=1:
        return str

    mid = len(str)//2
    
    left = merge_sort(str[:mid])
    right = merge_sort(str[mid:])
    
    return merge(left, right)
 
def merge(left, right):

    result = []
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
             result.append(left[i])
             i += 1
        else:
            result.append(right[j])
            j += 1

    if i == len(left):
        result.extend(right[j:len(right)])
    elif j == len(right):
        result.extend(left[i:len(left)])
    
    return result

num = int(input())
put = []

for _ in range(num):
    a, b = map(int, input().split())
    put.append([a,b])

for i, j in merge_sort(put):
    print(i,j)
