def solution(s):
    s=list(s)
    s.pop(0)
    s.pop(-1)
    reList = []
    temp =[]
    for i in s:
        if i=='{':
            temps = []
            temp = ''
        if i in ['0','1','2','3','4','5','6','7','8','9']:
            temp+=i
        if i ==',':
            temps.append(int(temp))
            temp = ''
        if i=='}':
            temps.append(int(temp))
            reList.append(temps)
    reList.sort(key=lambda x: len(x))
    answer=[]
    for i in range(len(reList)):
        for j in range(len(reList[i])):
            if reList[i][j] not in answer:
                answer.append(reList[i][j])
    return answer

    
print(solution('{{111}}'))