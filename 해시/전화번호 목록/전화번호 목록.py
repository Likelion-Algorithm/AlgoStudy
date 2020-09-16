
def solution(phone_book):
    phone_book_dict = {}

    for i in range(len(phone_book)):
        if len(phone_book[i]) == 1:
           for i in range(i+1, len(phone_book)):
               if phone_book[i][0] == phone_book[i]:
                   return False

        divide = 10**(len(phone_book[i])-2)

        if int(phone_book[i])// divide not in phone_book_dict:
            phone_book_dict[int(phone_book[i])//divide] = 1
        else:
            return False
    return True


print(solution(["97674223", "976124", "118"]))


#테스트 11 통과 못함(반례가 뭔지 모르겟뜸 ㅜㅠㅠㅠㅠ)