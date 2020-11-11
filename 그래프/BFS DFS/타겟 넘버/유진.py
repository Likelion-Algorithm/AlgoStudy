# 1번) 타겟넘버
# 통과
def solution(numbers, target):
    tree = [0]
    for num in numbers:
        new = []
        for leaf in tree:
            new.append(leaf+num)
            new.append(leaf-num)
        tree = new
    return new.count(target)
