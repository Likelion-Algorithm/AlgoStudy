def solution(people, limit):
    answer = 0
    people.sort()
    check = 0
    while people:
        temp = people.pop()
        index = 0
        while index != len(people):
            if temp + people[0] > limit:
                break
            # print(answer, people, check)
            if temp + people[index]<= limit:
                temp+= people[index]
                people.remove(people[index])
                if temp == limit:
                    break
                if index < len(people):
                    if temp + people[index]>limit:
                        break
            else:
                index+=1
        answer+=1
        
    return answer

# def solution(people, limit):
#     answer = 0
#     people.sort(reverse=True)
#     check = 0
#     while people:
#         temp = people.pop()
#         index = 0
#         while index != len(people):
#             if temp + people[-1] > limit:
#                 break
#             # print(answer, people, check)
#             if temp + people[index]<= limit:
#                 temp+= people[index]
#                 people.remove(people[index])
#                 if temp == limit:
#                     break
#                 if index < len(people):
#                     if temp + people[index]>limit:
#                         break
#             else:
#                 index+=1
#         answer+=1
# #         if check + people[0] <= limit and check!=0:
# #             check+= people.pop(0)
# #         elif check + people[-1] <= limit and check ==0:
# #             check += people.pop()
# #             answer+=1
# #         elif check + people[-1]<= limit and check!=0:
# #             check += people.pop()
        
        
#     return answer

# # def solution(people, limit):
#     answer = 0
#     check_list = []
#     while people:
#         temp = people.pop(0)
#         # check_list.append(temp)
#         index = 0
#         while index < len(people):
            
#             if people[index]+temp <=limit:
#                 temp+= people[index]
#                 people.remove(people[index])
#             else:
#                 index+=1
            
#         answer+=1
                
            
#     return answer