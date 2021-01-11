from itertools import combinations

temp = list(map(int,input().split()))
combination = []
while temp[0]!=0:
    combination.append(combinations(temp[1:],6))
    temp = list(map(int,input().split()))
for i in combination : 
    for j in i:
        for k in j:
            print(k, end=' ')
        print()
    print()

#단순히 조합 문제