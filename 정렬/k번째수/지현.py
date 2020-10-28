
def solution(array, commands):

    
    answer = []

    for i in range(len(commands)):

        tmp = []

        num1 = commands[i][0]
        num2 = commands[i][1]
        num3 = commands[i][2]

        tmp = sorted(array[(num1-1):(num2)])

        answer.append(tmp[num3-1])

    return answer

print(solution([1,5,2,6,3,7,4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

#코드 성공
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))