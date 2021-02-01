N = int(input())
parent, child = map(int,input().split())
n = int(input())
family = dict()
for i in range(n):
    a,b = map(int, input().split())
    family.setdefault(a, [])
    family[a].append(b)
    family.setdefault(b, [])
    family[b].append(a)
answer = 0
def DFS(before ,node, dest ,depth):
    global answer
    if node == dest:
        answer+=depth
        return 
    for i in family[node]:
        if i != before:
            DFS(node,i,dest,depth+1)
    else:
        return
DFS(0,parent,child,0)
if answer:
    print(answer)
else:
    print(-1)