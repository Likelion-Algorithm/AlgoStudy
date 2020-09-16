def solution(phone_book):
    for i in phone_book:
        length = len(i)
        for j in phone_book:
            if len(j)<length:
                continue
            else:
                if j == i:
                    continue
                if j[:length] == i:
                    print(i,j)
                    answer = False
                    return answer 
    answer = True
    return answer