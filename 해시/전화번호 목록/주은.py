
def solution(phone_book):
    answer = True
    phone_book.sort(key=len)

    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            place = phone_book[j].find(phone_book[i])
            if place == 0:
                answer = False
                return answer

    return answer


print(solution(["119", "97674223", "1195524421"]))
