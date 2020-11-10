def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        check = skill_trees[i].find(skill[0])
        result = True
        for j in range(1,len(skill)):
            index = skill_trees[i].find(skill[j]) # 없으면 -1
            if check > index and index != -1:
                result = False
                break
            if check ==-1 and index != -1:
                result = False
                break
            check=index
        if result == True :
            answer +=1 
    return answer