# 틀린게 아니라 한 단어 다 탐색 후에
# 그 단어에서 겹쳐서 시작하는 단어는 target_idx를 찾을 수 없음

from sys import stdin

def make_table(target_str):
    table = [0]
    j = 0
    for i in range(1, len(target_str)):
        # j가 0이 될 때까지 감소시키며 타겟 문자열과 같아질 수 있는지 확인
        while (j != 0) and (target_str[i] != target_str[j]):
            j -= 1
        if target_str[i] == target_str[j]:
            j += 1
            table.append(j)
        else:
            table.append(0)
    return table

def KMP(target_str, search_str, table):
    count = 0
    place = []
    target_idx = 0
    # while target_idx != len(target_str) - 1:
    for search_idx in range(len(search_str)):
        # print(target_str[target_idx], search_str[search_idx], place)
        if target_str[target_idx] == search_str[search_idx]:
            if target_idx == len(target_str) - 1:
                place.append(str(search_idx - len(target_str) + 2))
                target_idx = 0
                count += 1
            else:
                target_idx += 1
        else:
            target_idx = table[target_idx - 1] + 1
    return count, place

search_str = stdin.readline().strip('\n')
target_str = stdin.readline().strip('\n')

table = make_table(target_str)
count, place = KMP(target_str, search_str, table)
print(count)
print(" ".join(place))


