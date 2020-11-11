from collections import deque

def solution(begin, target, words):
    answer = 0; visited = [False] * len(words)
    queue = deque([[begin, 0]])  # deque 만들 때 주의
    while queue:
        curr_word, curr_dist = queue.popleft()
        if curr_word == target:
            answer = curr_dist
            break
        for i in range(len(words)):
            if visited[i] == False:
                cnt = 0
                for j in range(len(curr_word)):
                    if curr_word[j] != words[i][j]: cnt += 1
                    if cnt > 1: break
                if cnt == 1:
                    visited[i] = True
                    queue.append([words[i], curr_dist+1])
    return answer