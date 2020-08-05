import sys

num_stuff, weight = map(int, sys.stdin.readline().split())
stuffs = []
V = []
S = []
for i in range (weight+1):
    V.append(0)
    S.append([])

for i in range (num_stuff):
    w, v = map(int, sys.stdin.readline().split())
    stuffs.append([w, v])

for i in range (0, weight+1): #V[0] ~ V[weight] 구하기
    for j in range (num_stuff): #무게당 최대 가치 구할 때 모든 물건들 한 번씩 체크

        # 해당 물건을 현재 가방에 넣을 수 있는 경우
        if ((i - stuffs[j][0]) >= 0):
            # 배낭에 새로운 물건 넣지 않음
            if (V[i-1] > V[i - stuffs[j][0]] + stuffs[j][1]):
                tmp = V[i-1]
                if(V[i] < tmp):
                    V[i] = tmp
                    S[i] = S[i-1].copy()
            # 배낭에 새로운 물건 넣기(이전에 저장해놓은 무게당 최대 가치 사용)
            else:
                tmp = V[i - stuffs[j][0]] + stuffs[j][1]
                if(V[i] < tmp and (j not in S[i - stuffs[j][0]])):
                    V[i] = tmp
                    S[i] = S[i-stuffs[j][0]].copy()
                    S[i].append(j)

        # 해당 물건을 현재 가방에 넣을 수 없는 경우
        else:
            tmp = V[i-1]
            if(V[i] < tmp):
                V[i] = tmp
                S[i] = S[i-1].copy()

print(S)
print(V)
print(V[weight])