def solution(begin, target, words):
    stack = []
    visited = []
    stack.append([begin,0])
    visited.append(begin)
    if target not in words:
        return 0
    while stack:                #DFS를 실시한다.
        temp = stack.pop()
        if temp[0] == target:   #DFS 단계별로 target과 비교한다.
            break
        for word in words:      #stack에 push하는 단계에서 visited를 기록하여 최소성 보장
            if 판독(word,temp[0]) and word not in visited:  
                stack.append([word,temp[1]+1])
                visited.append(word)
    return temp[1]

def 판독(a,b):          #변환할 수 있는 단어인 지를 판독하는 함수
    temp = 0
    for i, j in zip(a,b):
        if i!=j:
            temp+=1
    if temp!=1:
        return 0
    else:
        return 1