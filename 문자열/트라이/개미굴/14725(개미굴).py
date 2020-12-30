import sys

N = int(sys.stdin.readline())
tmp = []

for _ in range(N):
    foods = sys.stdin.readline().rstrip().split()
    foods.pop(0)
    tmp.append(foods)
tmp.sort()

for i in range(len(tmp)):
    if i == 0:
        for j in range(len(tmp[i])):
            print('--'*j+tmp[i][j])
    else:
        cnt = 0
        for j in range(len(tmp[i])):
            if tmp[i][j] == tmp[i-1][j]:
                cnt = j+1
            else:
                break
        for k in range(cnt, len(tmp[i])):
            print('--'*k+tmp[i][k])

                



# import sys

# N = int(sys.stdin.readline())
# enterance = {}

# def Add(foods):
#     current = enterance

#     for food in foods:
#         if food not in current:
#             current[food] = {}
#         else:
#             current = current[food]
#     current['*'] = True


# for _ in range(N):
#     foods = sys.stdin.readline().rstrip().split()
#     K = foods.pop(0)
#     Add(foods)
#     enterance = sorted(enterance.items())

#     # for i in range(len(enterance)):
#     #     if enterance[i][0] != '*':
#     #         foods = enterance[i]

    
# print(enterance)