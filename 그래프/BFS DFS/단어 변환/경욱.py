from collections import deque
def solution(begin, target, words):
    deque1= [begin]
    check = [False for i in range(len(words))]
    answer = 0
    while deque1:
        temp_list = list()
        for a in range(len(deque1)):
            for i in range(len(words)):
                two_check = 0
                if words[i] == deque1[a] or check[i] == True:
                    continue
                else:
                    for j in range(len(words[i])):
                        if words[i][j] == deque1[a][j]:
                            two_check +=1
                        else:
                            continue
                    if two_check >=len(begin)-1:
                        temp_list.append(words[i])
                        check[i] =True
                        if words[i] == target:
                            return answer+1
                        
        answer+=1       
        deque1 = temp_list
                
    return 0