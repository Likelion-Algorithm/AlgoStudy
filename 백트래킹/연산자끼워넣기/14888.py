import sys

n = int(sys.stdin.readline())
num_arr = list(map(int, sys.stdin.readline().split()))
logic = list(map(int, sys.stdin.readline().split()))
logic_ = []

s = []
result = []

for i in range(4):
    for j in range(logic[i]):
        logic_.append(i)


def Problem():

    if len(s) == len(logic_):
        cnt = 0
        
        for i in range(len(s)):
            if i == 0:
                if logic_[s[i]] == 0:
                    cnt += num_arr[i] + num_arr[i+1]
                elif logic_[s[i]] == 1:
                    cnt += num_arr[i] - num_arr[i+1]
                elif logic_[s[i]] == 2:
                    cnt += num_arr[i] * num_arr[i+1]
                elif logic_[s[i]] == 3:
                    if num_arr[i]<0:
                        a= -(num_arr[i]) // num_arr[i+1]
                        cnt += -a
                    else:
                        cnt += num_arr[i] // num_arr[i+1]
            else:
                if logic_[s[i]] == 0:
                    cnt += num_arr[i+1]
                elif logic_[s[i]] == 1:
                    cnt -= num_arr[i+1]
                elif logic_[s[i]] == 2:
                    cnt *= num_arr[i+1]
                elif logic_[s[i]] == 3:
                    if cnt<0:
                        a= -(cnt) // num_arr[i+1]
                        cnt = -a
                    else:
                        a = cnt // num_arr[i+1]
                        cnt = a
        result.append(cnt)
        return

    for i in range(len(logic_)):
        if len(s) == 0:
            s.append(i)
            Problem()
            s.pop()
            
        else:
            if i in s:
                continue
            s.append(i)
            Problem()
            s.pop()

Problem()
print(max(result))
print(min(result))




