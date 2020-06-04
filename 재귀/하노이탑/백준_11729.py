def hanoi(n, beg, aux, end):
    result = []
    result_fin = []

    if n == 1:
        result.extend([beg, end])
        while True:
            result_fin.append(result)
            print(result_fin)
            break
    else:
        hanoi(n-1, beg, end, aux)
        hanoi(1, beg, aux, end)
        hanoi(n-1, aux, beg, end)
        

n = int(input())
hanoi(n,1,2,3)

