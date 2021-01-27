import sys
row = int(sys.stdin.readline())


def sol(temp):
    ab = temp[0][0]
    for i in range(len(temp)):
        for j in range(len(temp)):
            if ab != temp[i][j]:
                return False
            else:
                ab = temp[i][j]
    result[temp[0][0]] += 1
    return True


def divide(temp):
    temp_board = []
    ver = len(temp)//3
    for i in range(0, len(temp), ver):
        for j in range(0, len(temp[i]), ver):
            temp_list = []
            for k in range(ver):
                temp_list.append(temp[i+k][j:j+ver])
            temp_board.append(list(temp_list))
    return temp_board


board = []
for i in range(row):
    board.append(list(map(int, sys.stdin.readline().split())))
board = [list(board)]
result = [0, 0, 0]

while board:
    temp = board.pop()
    if sol(temp) == False:
        board.extend(divide(temp))
print(result[-1])
print(result[0])
print(result[1])
