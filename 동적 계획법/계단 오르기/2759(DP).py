import sys

def stair_DP(stair):
    
    score = [0] # n번째까지 계단의 최대점수
    for i in range(1,3):
        if i == 1: # 1번째 계단: 0번째에서 1번째로 가는 경우의 수 1가지 -> 1번째 계단 자기 자신
            score.append(stair[i])
        else: # 2번째 계단: 0번째-> 1번째 or 0번째 -> 1번째(둘 중 가장 큰 값)
            score.append(max((stair[i]+stair[i-1], score[i-2]+stair[i])))
    
    for i in range(3, len(stair)): 
        score.append(max((stair[i]+stair[i-1]+score[i-3]), stair[i]+score[i-2]))
        # max(직전 칸 계단에서 현재위치로 온 경우(현재계단+전계단+n-3번째 계단까지 최대점수), 전전 칸 계단에서 현재위치로 온 경우(현재계단 + n-2번째 계단까지 최대점수))
    return score[-1] #가장 마지막 수 반환



num = int(sys.stdin.readline())
stair = []

for _ in range(num):
    stair.append(int(sys.stdin.readline()))
stair.insert(0,0)  #출발점(0번째 인덱스)은 점수 없음 -> 0번째 인덱스에 0 삽입

print(stair_DP(stair))

