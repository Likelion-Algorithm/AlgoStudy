def solution(numbers):
    numbers_str = list(map(str, numbers))

    answer = sorted(numbers_str,key= lambda x: x*3,reverse=True) # 어떠한 원리로 n번씩 문자열을 반복하는지 이해 안감(1000이하의 수가 주어지므로 3을 곱함)

    return str(int(''.join(answer)))

    #구글링했씀. 이러한 방법 상상도 못했음 ㅠㅠ 천재인가.. 저런 생각이 어케 머리에서 바로 떠오르지...