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



while coin_amount >0:
    index = coin_list.pop()
    if coin_amount >= index :
        result = coin_amount // index
        coin_amount -= result * index
        count +=result


print(count)