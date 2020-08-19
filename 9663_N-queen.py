import sys
num = int(sys.stdin.readline())
all_list = []
for i in range(num+2):
    if i == 0 or i == num+1:
        all_list.append([False]*(num+2))
    else:
        all_list.append([0]*(num+2))
print(all_list)
num_list =[False]+([False]*num)
location = 0
count = 0
def DFS(distance, num_list, location):
    print(num_list,distance,location)
    if distance == 0:
        for i in range(1,len(num_list)):
            if num_list[i]==False:
                prev_location = location
                location = i
                num_list[i]=True
                distance += 1
                DFS(distance,num_list,location)
                distance-=1
                num_list[i]=False
                location = prev_location
                
    if distance == num:
        global count
        count+=1
        print(f'끝까지 감{count}')
        return
    
    else:
        for i in range(1,len(num_list)):
            if i == location or i ==location-1 or i == location +1:
                continue
            elif num_list[i] ==False:
                prev_location = location
                location=i
                num_list[i]=True
                distance+=1
                DFS(distance, num_list,location)
                num_list[i]=False
                distance-=1
                location= prev_location
            else:
                print('안된경우')
                return


DFS(0,num_list,location)
print(count)