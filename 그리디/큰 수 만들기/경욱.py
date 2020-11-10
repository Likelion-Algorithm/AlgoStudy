from itertools import combinations
def solution(number, k):
    answer = f'{number[0]}'
    # print(answer)
    length = len(number) - k
    
    for i in range(1,len(number)):
        while len(answer)>0 and k > 0 and answer[-1]< number[i]:
            # print(answer)
            k-=1
            answer = answer[:-1]
        answer += str(number[i])
    if k != 0:
        answer = answer[:-k]
    return answer


# from itertools import combinations
# def solution(number, k):
#     answer = f'{number[0]}'
#     # print(answer)
#     length = len(number) - k
    
#     for i in range(1,len(number)):
        
#             # for j in range(len(answer)-(len(number)-i),len(answer)):
#                 for j in range(len(answer)):    
#                     print(f'i={i} number[i]={number[i]}, j={j} answer[j] = {answer[j]} answer={answer}')
#                     if answer[j]<number[i]:
#                         if len(number) - i >= length-j:
#                             answer = answer[:j]+number[i]
#                             break
#                         else:
#                             if j == len(answer)-1 and len(answer) < length:
#                                 answer = answer + number[i]
#                                 break
#                     else:
#                         if j == len(answer)-1 and len(answer) < length:
#                             answer = answer + number[i]
            
#     return answer
# from itertools import combinations
# def solution(number, k):
#     # answer = max(map(''.join,list(combinations(number,len(number)-k))))
#     answer = f'{number[0]}'
#     length = len(number) - k
#     temp_first_index = 0
#     # for a in range(1, len(number)//2):
#     #     if number[a] > answer[0]:
#     #         temp_first_index = a
#     #         answer = number[a]
#     #     elif  number[a]== answer[0]:
#     #         answer = answer[:len(answer)]+number[a]
#     for i in range(1,len(number)):
#             for j in range(len(answer)):
#                 print(f'i={i} number[i]={number[i]}, j={j} answer[j] = {answer[j]} answer={answer}')
#                 if answer[j]<number[i]:
#                     if len(number) - i >= length-j:
#                         answer = answer[:j]+number[i]
#                         break
#                     else:
#                         if j == len(answer)-1 and len(answer) < length:
#                             answer = answer + number[i]
#                             break
#                 else:
#                     if j == len(answer)-1 and len(answer) < length:
#                         answer = answer + number[i]
                        
#     return answer