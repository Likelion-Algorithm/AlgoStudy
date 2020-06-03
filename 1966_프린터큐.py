import sys
num_input = int(sys.stdin.readline())
# num_list = [[1, 0], [4, 2], [6, 0]]
# weight_list= [[5], [1, 2, 3, 4], [1, 1, 9, 1, 1, 1]]
num_list,weight_list  = list(),list()
for i in range(num_input):
    num_list.append(list(map(int,sys.stdin.readline().strip().split())))
    weight_list.append(list(map(int,sys.stdin.readline().strip().split())))
    


def function(num_list, weight_list):
    print_index = 1
    num_list_index = num_list[1]
    while weight_list: 
        if max(weight_list) == weight_list[0]:
            if num_list_index == 0:
                print(print_index)
                break
            del weight_list[0]
            print_index +=1
            num_list_index-=1
        if max(weight_list) > weight_list[0]:
    
            weight_list.append(weight_list[0])
            del weight_list[0]
            if num_list_index == 0:
                num_list_index = len(weight_list)-1
            else:
                num_list_index -=1
        
for i in range(len(num_list)):
    function(num_list[i],weight_list[i])


