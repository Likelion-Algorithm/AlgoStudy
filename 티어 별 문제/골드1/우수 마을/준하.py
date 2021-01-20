# https://www.acmicpc.net/problem/1949


def answer(index):
    global G, V
    DP = [[0] * 2 for _ in range(n + 1)]

    for i in range(1, len(DP)):
        print(i)
        DP[i][1] = max([DP[k][0] for k in G[i]]) + V[i - 1]
        DP[i][0] = max([max(DP[k]) for k in G[i]])
    print(DP)


def dfs(index):
    global G, V, visited, DP

    visited[index] = True
    DP[index][1] = V[index - 1]

    for i in G[index]:
        if not visited[i]:
            dfs(i)
            DP[index][0] += max(DP[i])
            DP[index][1] += DP[i][0]


import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
V = list(map(int, input().split()))
G = {i + 1: set() for i in range(n)}
DP = [[0] * 2 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)
dfs(1)
print(max(DP[1]))
 47  practice/Greedy/Tree_traversal_1991.py 
@@ -0,0 +1,47 @@
# https://www.acmicpc.net/problem/1991

def preorder(node):
    global G, result
    if node == '.':
        return
    result.append(node)
    preorder(G[node][0])
    preorder(G[node][1])


def inorder(node):
    global G, result
    if node == '.':
        return
    inorder(G[node][0])
    result.append(node)
    inorder(G[node][1])


def postorder(node):
    global G, result
    if node == '.':
        return
    postorder(G[node][0])
    postorder(G[node][1])
    result.append(node)

import sys
input = sys.stdin.readline
n = int(input())
G = {}
for i in range(n):
    parent, left, right = input().split()
    G[parent] = [left, right]

result = []
preorder('A')
print(*result, sep='')

result.clear()
inorder('A')
print(*result, sep='')

result.clear()
postorder('A')
print(*result, sep='')
