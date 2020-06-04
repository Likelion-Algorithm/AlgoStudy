import sys
repeat = int(sys.stdin.readline().strip())
num_list = []
for i in range(repeat):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        num_list = num_list[:-1]
    else:
        num_list.append(num)
print(sum(num_list))
