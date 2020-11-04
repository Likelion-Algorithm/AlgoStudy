def solution(number, k):
    answer = ''
    left_index = 0; right_index = k+1; max_index = 0
    for _ in range(len(number) - k):
        max_num = "0"
        for i in range(left_index, right_index):
            if max_num < number[i]:
                max_num = number[i]
                if max_num == "9": 
                    max_index = i
                    break
        if max_num != "9":
            for i in range(left_index, right_index):
                if number[i] == max_num:
                    max_index = i
                    break
        left_index = max_index + 1; right_index += 1
        answer += max_num    
    return answer