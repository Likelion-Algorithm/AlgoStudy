import heapq

def solution(jobs):
    answer = 0
    length = len(jobs)
    count = 0
    jobs.sort(key = lambda x: x[0])
    while jobs:
        wait = []
        for i in range(len(jobs)):
            if 0 <=jobs[i][0] <=count :
                wait.append(jobs[i])
        if len(wait) == 0:
            count +=1
            continue
        # print(wait, present,answer)
        wait.sort(key= lambda x: x[1], reverse=True)
        temp = wait.pop()
        jobs.remove(temp)
        
            
        temp_post = count -temp[0]
        count +=  temp[1]
        answer += temp[1] + temp_post

    # print(jobs)
    return answer//length

# import heapq
# def solution(jobs):
#     answer = 0
#     distance=0
#     heapq.heapify(jobs)
#     heap = []
#     heap.append(heapq.heappop(jobs))
#     answer += heap[0][1]
#     distance += heap[0][1]
#     num = len(jobs)
    
#     print(answer)
#     while jobs:
#         temp_start = 0
#         temp_delay = 99999
#         temp_index = 0
#         for i in range(len(jobs)):
#             if jobs[i][0] > distance:
#                 continue
#             else:
#                 if jobs[i][1] < temp_delay:
#                     temp_delay = jobs[i][1]
#                     temp_index = i
#         temp = jobs.pop(i)
#         distance += temp[1]
#         answer = answer + distance - temp[0] + temp[1]
#         print(answer, distance,jobs)
                
            
    
    
#     return answer//num





# def solution(jobs):
#     jobs = sorted(jobs,  key = lambda x : (-x[1],-x[0]))
#     print(jobs)
#     answer = 0
#     # # heapq.heapify(jobs)
#     start_number = 0
#     while jobs:
#     #     # temp = heapq.heappop(jobs)
#         temp = jobs.pop()
#         dur=temp[1]
#         delay = temp[0]
#         answer = answer + dur +answer-delay
#     #     # answer+= take_time+answer - start_number 
#     #     print(temp,answer)
#     # print(jobs)
#     return answer//3