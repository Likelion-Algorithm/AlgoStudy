from itertools import combinations
import sys

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().split()))
operators = ['+', '-', 'x', '/']
operator_list = list(map(int, sys.stdin.readline().split()))

converted = [[1]*operator_list[0], [2]*operator_list[1], [3]*operator_list[2], [4]*operator_list[3]]
converted_list = []


for i in range(len(operator_list)): #연산자 모으는 for문
    for j in range(1,i+1):
        converted_list.append()


numbers_combination = list(combinations(numbers,2))


def operation(operator,a, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == 'x':
        return a*b
    else:
        return a // b

