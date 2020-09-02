import sys

string1 = sys.stdin.readline().strip()
string2 = sys.stdin.readline().strip()

answer = [0]*(len(string2)+1)

for i in string1:
    temp = answer[0]
    for j in range(len(string2)):
        temp1 = answer[j+1]
        if i == string2[j]:
            answer[j+1] = temp+1
        else:
            answer[j+1] = max(answer[j],answer[j+1])
        temp = temp1
print(max(answer))
