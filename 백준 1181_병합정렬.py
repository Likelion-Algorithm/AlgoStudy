num = int(input())
li = []

for i in range(num):
    Input = str(input()) 
    if Input not in li:
        li.append(Input)
def merge_sort(a):
    n = len(a)
    
    if n<=1:
        return a

    mid = n//2
    g1 = a[:mid]
    g2 = a[mid:]

    merge_sort(g1)
    merge_sort(g2)

    i1 = 0
    i2 = 0
    ia = 0

    while i1<len(g1) and i2<len(g2):
        if len(g1[i1]) < len(g2[i2]):
            a[ia] = g1[i1]
            ia += 1
            i1 += 1

        elif len(g1[i1]) == len(g2[i2]):
            if g1[i1] < g2[i2]:
                a[ia] = g1[i1]
                ia += 1
                i1 += 1

            else:
                a[ia] = g2[i2]
                ia += 1
                i2 += 1

        else:
            
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
            
    while i1<len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1

    while i2<len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1
    

merge_sort(li)   


for i in li:
    print(i)

