def solution(phone_book):
    phone_book.sort()
    d = dict()
    answer = True
    for i in phone_book:
        if not answer:
            break
        for j in range(len(i)):
            if j+1 in d.keys() and i[:j+1] in d[j+1]:
                answer = False
                break
        if len(i) in d.keys():
            d[len(i)]+=[i]
        else:
            d[len(i)]=[i]
    return answer