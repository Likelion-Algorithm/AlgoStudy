def solution(answer):

    from itertools import cycle

    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    answer_sheet = [0,0,0]
    people = []

    result = [list(zip(cycle(student1), answer)),list(zip(cycle(student2),answer)), list(zip(cycle(student3), answer))]

    for i in range(len(result)):
        for a,b in result[i]:
            if a == b:
                answer_sheet[i] += 1

    highest = max(answer_sheet)

    for i in range(3):
        if answer_sheet[i] == highest:
            people.append(i+1)

    return people

#통과
#아무리 생각해도 로직이 맞는데 자꾸 런타임 에러떠서 뭐가 잘못일까 생각해봤는데 수포자들의 답이 주기를 갖는다는 것을 간과해서 에러가 난거였다.
#cycle 함수 찾아봐서 알게됨. 이거 안쓰면 못풀듯..Zip 함수도 처음 알았드아..
