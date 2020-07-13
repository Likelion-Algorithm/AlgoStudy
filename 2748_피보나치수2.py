# def fib(num):
#     if num== 0:
#         return 0
#     if num == 1:
#         return 1
#     else:
#         return fib(num-2) + fib(num-1)
# for i in range(num_input):
#     print(fib(i), end =" ")
# print()
import sys
num_input = int(sys.stdin.readline())

num_1 = 0
num_2 = 0
answer = 0

for i in  range(num_input+1):
    if i == 0:
        answer =0
        continue

    if i ==1 :
        num_2 = 1
        answer = 1
    else:
        answer = num_1 + num_2
        num_1,num_2  = num_2, answer
print(answer)
