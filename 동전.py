import sys
num_input = list(map(int,sys.stdin.readline().split()))


coin_num = num_input[0]
coin_amount = num_input[1]
coin_list = []

for i in range(coin_num):
    temp = int(sys.stdin.readline())
    if temp <= coin_amount:
        coin_list.append(temp)

count = 0
print(coin_list)

for i in range()
while coin_amount >0:
    index = coin_list.pop()
    if coin_amount >= index :
        while coin_amount >= index:
            coin_amount -= index
            count +=1


print(count)