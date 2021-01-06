n = int(input())
answer = [0,1,1,1,1,1,1,1,1,1]

for i in range(1,n):
    temp = [0]*10
    for j in range(10):
        if j==0:
            temp[j]=answer[1]
        elif j==9:
            temp[j]= answer[8]
        else:
            temp[j] = answer[j-1]+answer[j+1]
    answer = list(temp)
print(sum(answer)%1000000000)