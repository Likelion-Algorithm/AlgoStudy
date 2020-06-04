import sys
size,out = map(int,sys.stdin.readline().strip().split())
out_num = list(map(int,sys.stdin.readline().strip().split()))
cnt = 0
rotate_queue = [i+1 for i in range(size)]
for i in out_num:
    INDEX = rotate_queue.index(i)
    if INDEX > len(rotate_queue)//2:
        cnt += len(rotate_queue) - INDEX
        rotate_queue = rotate_queue[INDEX:]+rotate_queue[:INDEX]
        rotate_queue.remove(i)
    else:
        cnt += INDEX
        rotate_queue = rotate_queue[INDEX:] + rotate_queue[:INDEX]
        rotate_queue.remove(i)
print(cnt)