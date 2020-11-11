def solution(numbers, target):
    answer = 0
    stack = [0,1]
    visited = []
    while stack:                    #DFS실시 후 최대 깊이에서 연산 한다.
        temp = stack.pop()
        visited.append(temp)
        if len(visited)!=len(numbers):
            stack.extend([0,1])
        else:
            if cal(visited, numbers)==target:
                answer+=1
            while visited and visited[-1]==0:
                visited.pop()
            if visited:
                visited.pop()

    return answer

def cal(stack, numbers):            # +(1)와 -(0)을 조합해 계산한 값을 반환하는 함수
    temp = 0
    for i in range(len(stack)):
        if stack[i]:
            temp+=numbers[i]
        else:
            temp-=numbers[i]
    return temp