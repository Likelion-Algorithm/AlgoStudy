import sys
sys.setrecursionlimit(10**6)

N = int(input())
tree = dict()
answer = [0]*(N+1)
for i in range(N-1):
    x,y = map(int, input().split())
    tree.setdefault(x,[])
    tree[x].append(y)
    tree.setdefault(y,[])
    tree[y].append(x)
def order(before, node):
    global answer, tree
    answer[node]=before
    for i in tree[node]:
        if i!=before:
            order(node, i)
order(0,1)
for i in range(2, N+1):
    print(answer[i])