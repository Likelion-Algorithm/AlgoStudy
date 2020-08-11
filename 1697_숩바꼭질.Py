import sys
a,b = list(map(int,sys.stdin.readline().split()))

room = [False]*100001
def BFS(a,b):
    count = 0
    visited,need_visit = list(),list()
    need_visit.append(a)
    while need_visit:
        
        temp_list = []
        for i in need_visit:
            if i == b:
                print(count)
                return
            if i*2 <= 100000 and room[i*2] == False:
                room[i*2] = True
                temp_list.append(i*2)
            if i>0 and room[i-1] == False:
                room[i-1] = True
                temp_list.append(i-1)
            if i <100000 and room[i+1] == False:
                room[i+1] = True
                temp_list.append(i+1)
        count +=1 
        need_visit = temp_list
BFS(a,b)