def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        temp = []
        for j in skill:
            if j in i:
                temp.append(i.index(j))
            else:
                temp.append(float('inf'))
        answer+= [0,1][temp==sorted(temp)]
    return answer