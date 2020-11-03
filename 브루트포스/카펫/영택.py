def solution(brown, yellow):
    answer = []
    candidate_yellow_pair = get_aliquot(yellow)
    for x in candidate_yellow_pair:
        yellow_width, yellow_height = x
        if yellow_width + yellow_height == (brown - 4) // 2:
            if yellow_width * yellow_height == yellow:
                answer.extend([yellow_width+2, yellow_height+2])
                break
    return answer

def get_aliquot(num:int) -> [tuple]:
    result = []
    for i in range(1, num+1):
        remainder = num % i; quotient = num // i 
        if remainder == 0 and i >= quotient:
            result.append((i, quotient))  # (candidate_yellow_width, candidate_yellow_height)
    return result
