import sys

n ,k = sys.stdin.readline().split()
n = int(n)
k = int(k)
# all_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

w_list = list()
v_list = list()
all_list = list()

# 무게 따로 가치 따로 리스트 만들어줌
for i in range(n):
    c, d = sys.stdin.readline().split()
    w_list.append(int(c))
    v_list.append(int(d))
    all_list.append((int(c),int(d)))

#최대구간의 합 DP사용해서 구해보기
def max_interval(v_list, w_list):
    S = [0]*len(v_list) #초기화
    S[0] = v_list[0] #바닥조건 설정
    for k in range(n):
        # if
        S[k] = max(S[k-1] + v_list[k], v_list[k]) #점화식

    W = [0]*len(w_list)
    W[0] = w_list[0]
    # W[k]는 w_list[k]로 끝나는 무게 리스트의 합
    for k in range(n):
        W[k] = max(W[k-1] + w_list[k] , w_list[k])
    print(S)

    return max(S)

print(max_interval(v_list, w_list))
