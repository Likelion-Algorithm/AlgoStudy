import sys
num_input = int(sys.stdin.readline())
wait_list = list(map(int,sys.stdin.readline().split()))

wait_list.sort()
time_list = []
time = 0
for i in wait_list:
    time += i
    time_list.append(time)
    
print(sum(time_list))

ㅠ  