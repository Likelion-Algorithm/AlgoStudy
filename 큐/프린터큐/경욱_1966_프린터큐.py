import sys
num_input = int(sys.stdin.readline())
# num_list = [[1, 0], [4, 2], [6, 0]]
# weight_list= [[5], [1, 2, 3, 4], [1, 1, 9, 1, 1, 1]]
num_list,weight_list  = list(),list()
for i in range(num_input):
    num_list.append(list(map(int,sys.stdin.readline().strip().split())))
    weight_list.append(list(map(int,sys.stdin.readline().strip().split())))
    


def function(num_list, weight_list):
    # 결과값 변수
    print_index = 1
    # 결과값 위치 변수
    num_list_index = num_list[1]
    while weight_list:
        # 중요도가 제일 높은게 리스트 맨 앞에 와있는경우 
        if max(weight_list) == weight_list[0]:
            # 결과값위치가 0일때 출력하고 끝
            if num_list_index == 0:
                print(print_index)
                break
            del weight_list[0]
            # 출력 횟수 올라감
            print_index +=1
            # 결과값 위치는 리스트 앞으로 한칸 이동
            num_list_index-=1
            # 리스트 맨 앞의 중요도가 낮은경우
        if max(weight_list) > weight_list[0]:
            # 뒤로 추가해주고
            weight_list.append(weight_list[0])
            # 앞에꺼는 없애버림
            del weight_list[0]
            # 결과값이 중요도 보다 낮으므로 뒤로 보내버리고 위치도 0이 아닌 리스트 끝으로 다시 변환
            if num_list_index == 0:
                num_list_index = len(weight_list)-1
            else:
            # 아니면 그냥 앞으로 한칸 밀어내기 
                num_list_index -=1
        
for i in range(len(num_list)):
    function(num_list[i],weight_list[i])


