import sys
from itertools import combinations

# 아이디어: 가능한 모든 item들의 조합의 index를 구해서 이것을 다 더한 것들 중 max를 찾아 return
# 처음에는 dp의 특징을 활용해 표를 그려 해를 찾으려고 했지만 순차적인 조합만을 커버할 수 있었고
# 임의의 조합은 커버할 수 없다는 문제점이 있었다.

N, K = list(map(int, sys.stdin.readline().split()))
x_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] #w와v의 조합 input

N_list = [i for i in range(N)]
sol_list= list() # 모든 가능한 조합의 집합

for  i in range(1, N): #0부터 하면 공집합이 생기기 때문에 이를 처리하려면 1부터 설정
    N_combinations = [list(x)for x in combinations(N_list, i)]
    sol_list.extend(N_combinations)

fin_list = list()
w_sum = 0
v_sum = 0
while sol_list:
    temp = sol_list.pop()
    for i in temp: #인덱스를 실제 조합과 매칭
        w_sum += x_list[i][0]
        if w_sum  <= K :
            v_sum += x_list[i][1]
        else:
            w_sum -= x_list[i][0]

    fin_list.append((w_sum, v_sum))
    w_sum = 0
    v_sum = 0

a, b = max(fin_list)
print(b)




import sys

# 인터넷 참고
# 아이디어 : dp표를 1~k까지 무게를 기준으로 둘면서
# 현재 물건이 가방 속 물건보다 작다면 이전 값 그대로 가져온다
# 그렇지 않으면, (1)현재 물건을 넣어준 후, 남은 무게를 채울 수 있는 최댓값을 더해준다
# (2) 다른 물건들로 채워준다
# (1) 과 (2) 중 더 큰 값을 knapsack에 저장
![12](https://user-images.githubusercontent.com/59404684/91967638-71298580-ed4e-11ea-8938-4fd89154550f.PNG)

n, k = map(int, sys.stdin.readline().split())
stuff =[[0, 0]]
for _ in range(n):
    stuff.append(list(map(int, sys.stdin.readline().split())))

knapsack = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if weight > j:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value+ knapsack[i-1][j-weight], knapsack[i-1][j])
        #이전 행 중에서 j-weight에 해당하는 열을 선택

print(knapsack[n][k])
