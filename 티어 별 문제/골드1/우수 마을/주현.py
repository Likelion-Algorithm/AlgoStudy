from collections import deque
import sys
sys.setrecursionlimit(10**6)

N = int(input())
values = list(map(int, input().split()))
values.insert(0,0)
DP = [0]*(N+1)
tree = dict()
for i in range(N-1):                        #트리구성
    a, b = map(int, input().split())
    if a in tree.keys() and b not in tree[a]:
        tree[a].append(b)
    else:
        tree[a] = [b]

    if b in tree.keys() and a not in tree[b]:
        tree[b].append(a)
    else:
        tree[b] = [a]

def Cuscal(node):                            #인접 노드의 dp값을 덧셈
    if tree[node] == [node]:
        return 0
    temp = 0
    for i in tree[node]:
        if i != node and DP[i]!=0:
            temp += DP[i]
    return temp

def Postorder(before , node):                 #후위순회 + 점화식
    if tree[node]==[before]:
        DP[node] = values[node]
        return 0
    temp = 0
    for after in tree[node]:
        if after != before:
            Postorder(node , after)
            temp += Cuscal(after)
    DP[node] = max(temp+values[node],Cuscal(node))

Postorder(0, 1)
print(DP[1])