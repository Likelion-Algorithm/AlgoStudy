def solution(answers):
    score = []
    supoza = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    for student in supoza:
        correct = 0
        for i in range(len(answers)):
            if answers[i]==student[i%len(student)]:
                correct+=1
        score.append(correct)
    m= max(score)
    answer = [i+1 for i, j in enumerate(score) if j == m]
    return answer