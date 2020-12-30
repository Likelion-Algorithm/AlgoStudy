import sys

N = int(sys.stdin.readline())
words = []
check = []
answer = {}
cnt = 0
checker = False

for _ in range(N):
    words.append(sys.stdin.readline().rstrip())

for i in range(len(words)):
    word = words[i]
    for j in range(len(word)):
        if j == 0:
            check.append(word[j])
            answer[word[j]] = 1
        else:
            if word[j] in check and word[j] in answer:
                answer[word[j]] += 1
            elif word[j] not in answer:
                check.clear()
                check.append(word[j])
                answer[word[j]] = 1
            elif word[j] not in check and word[j] in answer:
                checker = True
                break
    if checker == False:
        cnt += 1
    else:
        checker = False
    answer.clear()
    check.clear()    
    
print(cnt)

#통과