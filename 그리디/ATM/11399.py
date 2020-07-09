num = int(input())

time = map(int, input().split())
time_sort = sorted(time)

waiting_time = 0

for i in range(num):
    a = time_sort[0:i+1]
    waiting_time += sum(a)

print(waiting_time)




