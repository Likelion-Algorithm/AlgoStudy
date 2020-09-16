def solution(genres, plays):
    d= dict()
    s= dict()
    answer = []
    for i in range(len(genres)):
        d[genres[i]]=[]
        s[genres[i]]=0
    for i in range(len(genres)):
        d[genres[i]].append([i,plays[i]])
        s[genres[i]]+= plays[i]
    s = sorted(s.items(), key= lambda x:x[1],reverse=True )
    for i in s:
        temp = sorted(d[i[0]],key = lambda x:(-x[1],x[0]))
        if len(temp)>1:
            answer.append(temp[0][0])
            answer.append(temp[1][0])
        else:
            answer.append(temp[0][0])
    return answer