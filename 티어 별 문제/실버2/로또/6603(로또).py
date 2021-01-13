import sys

from itertools import combinations

def lottos(array):
    combi = list(combinations(array, 6))

    for i in combi:
        for j in i:
            print(j, end=' ')
        print()


while True:
    S = list(map(int, sys.stdin.readline().split()))

    if S[0] != 0:
        S.pop(0)
        lottos(S)
        print()
    else:
        break

#end=' ' 공백을 안 넣어줘서 계속 틀린 문제^^ 공백을 잘 살피자^^
#dfs(재귀).ver
# import sys

# answer = [0]

# def lotto(S):
#     if len(answer) == 7:
#         for i in range(1,7):
#             print(answer[i], end=' ')
#         print()
#         answer.pop()
#     else:
#         for i in range(len(S)):
#             if S[i] not in answer and answer[-1]<S[i]:
#                 answer.append(S[i])
#                 lotto(S)
                
#         answer.pop()



# while True:
#     S= list(map(int, sys.stdin.readline().split()))
#     if S[0] != 0:
#         k = S.pop(0)
#         lotto(S)
#         answer = [0]
#         print()
#     else:
#         break
    
    