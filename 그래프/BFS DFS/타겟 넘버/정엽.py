def regre(numbers, target, index, countedNum):
    if index == len(numbers):
        if countedNum == target:
            return 1
        else:
            return 0
    return regre(numbers, target, index + 1, countedNum + numbers[index]) + regre(numbers, target, index+1,countedNum - numbers[index])


def solution(numbers, target):
    answer = 0
    answer = regre(numbers, target, 0, 0)
    return answer