import sys

N = int(sys.stdin.readline())
answer = [([0]*10) for _ in range(N)]

for i in range(N):
    for j in range(10):
        
        if i==0:
            if j==0:
                answer[i][j] = 0
            else:
                answer[i][j] = 1
        else:
            if j==0:
                answer[i][j] = answer[i-1][j+1]
            elif j == 9:
                answer[i][j] = answer[i-1][j-1]
            else:
                answer[i][j] = answer[i-1][j-1]+ answer[i-1][j+1]

print(sum(answer[N-1])%1000000000)
#통과

#계단식이 될려면 '어떤 수'와 '그 수 앞자리'의 차이가 -1 or +1이 나면 된다. 따라서 마지막 자리의 수를 기준으로 생각하게 되면
#마지막 수의 앞 자리는 이전 수(-1인덱스)에서 마지막 수보다 1이 작거나 1이 큰 수가 오면 되므로 answer에서 해당 인덱스이 수를 더해주면 된다(answer은 '마지막 숫자' 기준이므로 해당 수는 j 인덱스를 마지막으로 갖는 i자리 수)