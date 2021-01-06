import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.insert(0,0)
answer = [0]*(N+1)

for i in range(1, len(cards)):
    if i == 1:
        answer[i] = cards[i]
    else:
        num = i//2
        tmp = [cards[i]]
        for j in range(1, num+1):
            tmp.append((answer[i-j]+answer[j]))
        answer[i] = max(tmp)

print(max(answer))
#통과


#처음에 푼 것(틀림)
# N = int(sys.stdin.readline())
# cards = list(map(int, sys.stdin.readline().split()))
# cards.insert(0,0)
# answer = [0]*(N+1)

# for i in range(1, N+1):
#     q = N//i
#     r = N%i
    
#     answer[i] = (cards[i]*q)+cards[r]

# print(max(answer))

#처음에는 그냥 나눗셈을 활용해서 접근했는데 예제는 다 맞지만 24%에서 틀렸습니다가 뜨길래 dp방식대로 각 카드를 n개씩 뽑았을 때의 최대값을 저장해주는 방식으로 품
