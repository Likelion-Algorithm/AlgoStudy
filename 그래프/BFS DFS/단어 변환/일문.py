# 실패

def search(b, t, w):
    cnt = 0
    candidate =[]
    for a in w: # 리스트 순환
        for i in range(len(a)): # 단어 내 글자 순환
            if a[i] == b[i]:
                cnt +=1
        if cnt >= 2:
            w.remove(a)
            return a
def solution(begin, target, words):
    answer = 0
    w_cnt = 0
    for _ in range(len(words)):
        x = search(begin, target, words)
        w_cnt += 1
    answer = w_cnt
    return answer