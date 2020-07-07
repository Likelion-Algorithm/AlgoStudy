import sys

def average(nums):
    if len(nums) == 1:
        return nums[0]

    result = round(sum(nums)/len(nums))
    return result

def middle(nums):
    if len(nums) == 1:
        return nums[0]

    mid = len(nums)//2
    result = sorted(nums)
    return result[mid]

def frequency(nums):
    if len(nums) == 1:
        return nums[0] #리스트 내에 값이 1개밖에 없을 땐 그대로 반환

    dic = {}

    for number in nums:
        if number in dic:
            dic[number] += 1
        else:
            dic[number] = 1 #숫자:key, 출현 빈도수:value
    
    dic_frequency = max(dic.values())
    temp = []

    for i, j in dic.items():
        if j == dic_frequency:
            temp.append(i) #value(빈도수)의 최대값을 구해 해당 value의 key를 임시 리스트에 보관
            

    temp_sorted = sorted(temp) #오름차순으로 정렬

    if len(temp_sorted) == 1: 
        return(temp_sorted[0]) #temp안에 값 하나면 인덱스 0번째 값 출력

    return(temp_sorted[1]) # 그 외에는 두 번째로 작은 값인 인덱스 1번째 값 출력

def range_(nums):
    return max(nums) - min(nums)

number = int(sys.stdin.readline())
str = []

for _ in range(number):
    str.append(int(sys.stdin.readline()))


print(average(str))
print(middle(str))
print(frequency(str))
print(range_(str))