import sys
num = int(sys.stdin.readline())
board = list(map(int, sys.stdin.readline().split()))
check = [False for _ in range(num)]


def dfs(num, depth, temp, result):
    if depth == num:
        comp = 0
        for i in range(len(temp)-1):
            comp += abs(temp[i]-temp[i+1])
        if comp > result:
            result = comp
        return result
    for i in range(len(check)):
        if check[i] == False:
            check[i] = True
            temp.append(board[i])
            result = dfs(num, depth+1, temp, result)
            temp.pop()
            check[i] = False

    return result


result = -999999
b = dfs(num, 0, [], result)
print(b)
