N = int(input())
paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))
answer = [0]*3

def cut(graph,n):
    total = 0
    a = graph[0][0]
    for i in graph:
        total+=i.count(a)
    if total == n*n:
        answer[a]+=1
        return 
    else:
        for i in range(0,n,n//3):
            for j in range(0,n,n//3):
                cut([row[j:j+(n//3)] for row in graph[i:i+(n//3)]],n//3)
cut(paper,N)
print(answer[-1])
print(answer[0])
print(answer[1])