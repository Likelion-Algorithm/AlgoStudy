def find(num,queue):
    time = 0
    visited = defaultdict(int)
    visited[queue[0]] = []
    while queue:
        temp = []
        time+=1
        for i in queue:
            if i > num:
                if visited[i-1] == []:
                    continue
                elif i-1 == num:
                    return time
                else:
                    visited[i-1] = []
                    temp.append(i-1)
            else:
                for j in [-1,1,i]:
                    if i+j in visited:
                        continue
                    elif i+j == num:
                        return time
                    else:
                        visited[i+j] = []
                        temp.append(i+j)
        queue = temp[:]




import sys
from collections import defaultdict
i, u = map(int,sys.stdin.readline().split())
queue = [i]
if i==u:
    print(0)
else:
    print(find(u,queue))