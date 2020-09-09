import sys

n = int(sys.stdin.readline())
amount = []
result = [0]*(n+1)
tmp = []

for _ in range(n):
    amount.append(int(sys.stdin.readline()))
amount.insert(0,0)

def DP_1(n):
    if n == 3:
        tmp.append(amount[n]+amount[n-1])
    else:   
        for i in range((n-3),0,-1):
            tmp.append(amount[n]+amount[n-1]+result[i])

def DP_2(n):
    for i in range((n-2),0,-1):
        tmp.append(amount[n]+result[i])

for i in range(1, n+1):
    if i <=2:
        result[i] = amount[i-1]+amount[i]
    else:
        DP_1(i)
        DP_2(i)
        result[i] = max(tmp)
        tmp = []

print(max(result))
    
#n번째 포도주까지 마셨을 때의 가능한 최대값을 result에 저장한다
#이때 n번째 포도주에서 가능한 최대값의 경우는 두가지이다.(3잔 연속으로 마시는 것이 안되므로) 
# n번째 포도주에서 가능한 최대값을 M(n)이라고 하면, 1) N(n)+N(n-1)+M((n-3)~1) 2) N(n)+ M((N-2)~1)->마시지 않는 포도주의 수에는 제한이 없으므로
# 따라서 for문을 통해 DP_1과 DP_2에 넣어 n번째 포도주의 최대값을 구한 뒤, 최대값들을 리스트에 넣은 후 max함수에 넣어 답을 찾는다.


#(시간초과가 떠서 pypy로 돌렸는데 돌아간다. 두개의 함수를 돌리지 않고도 해결할 수 있는 더 나은 방법이 있을 듯 하다.)
         
        














'''
for i in range(1,n+1):
    if cnt<2:
        if result[i-1]+amount[i] == result[i-1]:
            result[i] = result[i-1]
            cnt = 0
        else:
            result[i] = max(result[i-1]+amount[i], result[i-1])
            cnt += 1

    else:
        result[i] = result[i-1]
        cnt = 0

print(max(result))
        if result[i] == result[i-1]+amount[i]:
            cnt += 1
        
    else:
        result[i] = result[i-1]
'''


