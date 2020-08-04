import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    a,b = map(int,sys.stdin.readline().strip().split())
    standard = [i==b for i in range(a)]
    print(standard)
    priority = list(map(int,sys.stdin.readline().strip().split()))
    print(priority)
    print(priority[0])
    print(priority[0] == max(priority))
    cnt = 0;
    while True:
        if priority[0] == max(priority):
            if standard[0] == 'True':
                print(cnt)
                break
            del standard[0]
            del priority[0]
            cnt += 1
        else:
            priority.append(priority[0])
            standard.append(standard[0])
            del standard[0]
            del priority[0]