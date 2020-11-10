def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        temp=0
        bp=True
        if bp:
            for j in i:
                if j in skill and temp==skill.index(j):
                    temp+=1
                    continue
                elif j not in skill:
                    continue
                else:
                    bp=False
                    break
            if j==i[-1] and bp!=False:
                answer+=1         
        else:
            break
    return answer
