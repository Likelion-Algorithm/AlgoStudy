minus = input().split('-')

result = []

for i in range(len(minus)):
    if i == 0:
        result.append(sum(map(int, (minus[i]).split('+'))))
    else:
        plus = map(int, (minus[i]).split('+'))
        plus_with_minus = -(sum(plus))
        result.append(plus_with_minus)

print(sum(result))





