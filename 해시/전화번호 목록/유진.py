def solution(phone_book):
    phone_nums = list(num for num in phone_book)
    for num in phone_nums:
        for other in phone_nums:
            if (other != num) & (other.startswith(num)):
                return False
    return True
