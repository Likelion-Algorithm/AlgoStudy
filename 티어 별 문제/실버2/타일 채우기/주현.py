N = int(input())
hellDP = [0,0,3]
answer = 0
if N%2==0:
    for i in range(4,N+2,2):
        hellDP.append(0)
        temp = hellDP[2]*hellDP[i-2]
        for j in range(4,i,2):
            temp += 2*hellDP[i-j]
        hellDP.append(temp+2)
    answer = hellDP[N]
print(answer)