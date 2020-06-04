import sys
num_input = int(sys.stdin.readline())
num_list = list()
for i in range(num_input):
    numbers = int(sys.stdin.readline().strip())
    # 0이 아니면 추가해주기
    if numbers !=0:
        num_list.append(numbers)
    if numbers == 0:
        # 0이면 앞의 숫자를 빼버리기
        num_list.pop()
print(sum(num_list))











    