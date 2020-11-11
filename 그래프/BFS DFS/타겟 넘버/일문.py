def solution(numbers, target):
    result_list = [0]

    # i는 numbers의 각 원소들
    for i in range(len(numbers)):
        temp_list = []

        for j in range(len(result_list)):
            temp_list.append(result_list[j] - numbers[i])
            temp_list.append(result_list[j] + numbers[i])
        result_list = temp_list

    return result_list.count(target)