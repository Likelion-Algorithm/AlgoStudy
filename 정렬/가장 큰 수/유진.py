# 2번) 가장 큰 수
def solution(numbers):
    numbers = list(map(str,numbers))
    a = sorted(numbers, key=lambda x: (x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)]),reverse=True)
    answer = ''.join([str(i) for i in a])
    if int(answer)!=0: return answer
    else: return '0'
