num = int(input())

triangle = []
result = [0]

for _ in range(num):
    triangle.append(list(map(int, input().split())))


for i in range(1, num):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] = triangle[i-1][j] + triangle[i][j] # 왼쪽 끝 숫자 
        elif j == len(triangle[i])-1:
            triangle[i][j] = triangle[i-1][j-1] + triangle[i][j] # 오른쪽 끝 숫자
        else:
            triangle[i][j] = max(triangle[i][j] + triangle[i-1][j-1], triangle[i][j] + triangle[i-1][j]) 
            # 가운데 숫자들은 2개의 가능한 윗 단계 경로에서 max를 찾아 더하면 됨

print(max(triangle[-1]))


#양쪽 끝 숫자에 도착하는 방법은 각각 1가지 뿐(끝 경로만 이용하는 방법)
#따라서 양쪽 끝 애들은 끝 애들끼리만 더해주면 됨
#중간 애들은 도착하는 방법이 2개씩 - 따라서 윗 단계에서 더 큰 합을 만들 수 있는 애가 오면 됨
