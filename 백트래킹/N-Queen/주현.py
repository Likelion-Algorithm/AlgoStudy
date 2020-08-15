import time
start = time.time()
def nqueen(stack,queen,num):
    count = 0
    while stack:
        i,j = stack.pop()
        queen = {key: value for key, value in queen.items() if key < i}
        queen[i]=j
        if i==num-1:
            count+=1
        else:
            i+=1
            for j in range(num):
                if j not in {queen.values()}:
                    temp = True
                    for a,b in queen.items():
                        if i==a or j==b or abs(i-a)==abs(j-b):
                            temp = False
                            break
                    if temp:
                        stack.append([i,j])
    return(count)
num = int(input())
board = []
stack = []
queen = {}
for i in range(num):
    board.append([0]*num)
if num%2==0:
    for i in range(num//2):
        stack.append([0,i])
    count = nqueen(stack,queen,num)*2
else:
    for i in range(num//2):
        stack.append([0,i])
    count = nqueen(stack,queen,num)*2
    stack =[[0,num//2]] 
    queen = {}
    count+= nqueen(stack,queen,num)
print(count)
print("time :", time.time() - start)

              