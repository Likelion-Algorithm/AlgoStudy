import sys
num, dist = list(map(int,sys.stdin.readline().split()))
num_list =[False]+([False]*num)
result_list =[]

def DFS(distance, num_list, result_list):
  if distance == dist:
    print(" ".join(map(str,result_list)))
    return
  else:
    for i in range(1,len(num_list)):
      if num_list[i]==False:
        result_list.append(i)
        num_list[i]=True
        distance+=1
        DFS(distance, num_list,result_list)
        result_list.pop()
        num_list[i]=False
        distance-=1


DFS(0,num_list,result_list)