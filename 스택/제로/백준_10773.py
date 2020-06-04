n = int(input())
string = []

def stack(s):

    for num in range(n):            #n번만큼 nums를 입력받음
        nums=int(input())

        if nums!=0:
            string.append(nums)    # 입력한 숫자가 0이 아니면 리스트에 추가
        else:
            string.pop()
                                    #입력한 숫자가 0이라면 리스트 맨 뒤에 숫자 없앰
    return(string)   


print(sum(stack(string)))           #string 리스트의 요소들을 모두 더함

    


    


