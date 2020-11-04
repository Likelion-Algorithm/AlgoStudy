#  경로에 a가 있는경우
# 위로 갈지 아래로 갈지 설정
#   1 2 3 4 5 6 7 8 9  10 11 12          12 11 10 9  8  7  6  5  4   3  2  1
# A B C D E F G H I J  K  L  M    N(기준)O  P  Q  R  S  T  U  V  W   X  Y  Z
# 1 2 3 4 5 6 7 8 9 10 11 12 13   14     15 16 17 18 19 20 21 22 23  24 25 26
# B A A B A A A A A A B 11 11 13
#  경로에 a가 있는경우
# 위로 갈지 아래로 갈지 설정
#   1 2 3 4 5 6 7 8 9  10 11 12          12 11 10 9  8  7  6  5  4   3  2  1
# A B C D E F G H I J  K  L  M    N(기준)O  P  Q  R  S  T  U  V  W   X  Y  Z
# 1 2 3 4 5 6 7 8 9 10 11 12 13   14     15 16 17 18 19 20 21 22 23  24 25 26
# B A A B A A A A A A B 11 11 13
def solution(name):
    answer = 0
    check =[]
    length = len(name)
    for i in range(len(name)):
        if i == 0:
            check.append(i)
        elif name[i] != "A":
            check.append(i)
    index = 0
    while check:
        print(check,answer)
        if index == -1:
            temp = check[index]
            temp_prev = check[index-1]
            answer += temp-temp_prev
            calc = check.pop()
            index = -1
        else:
            temp = check[index]
            temp_prev = check[index-1]
            temp_next = check[index+1]
            if temp_next-temp > temp + length - temp_prev: # 0번에서 커서 왼쪽으로
                answer += temp+length - temp_prev
                calc = check.pop(0)
                index =-1
            elif temp_next-temp <= temp + length - temp_prev: # 0번에서 커서 오른쪽
                answer += temp_next - temp
                calc = check.pop(0)
                
        if ord(name[calc]) >= ord("N"):
            answer += 91 - ord(name[calc])
        elif ord(name[calc])== 65:
            continue
        else:
            answer += ord(name[calc])- 65
        # print('여기 확인', check, answer)
        
        if len(check) == 1:
          hoo = check.pop()
          print(check)
          if ord(name[hoo]) >= ord("N"):
            answer += 91 - ord(name[hoo])
          elif ord(name[hoo])== 65:
              continue
          else:
              answer += ord(name[hoo])- 65
          break
        # elif index == 0 and check[index]!=0:
        #     temp = check[index]
        #     temp_next = check[index+1]
    
    return answer
# def solution(name):
#     answer = 0
#     index = 0
#     cursor_count = 0
#     A_count = list(name).count("A")
    
        
#     while cursor_count != (len(name)-A_count):
#         print(answer, cursor_count)
        # if ord(name[index]) >= ord("N"):
        #     answer += 91 - ord(name[index])
#             if index < 0 :
#                 index -=1
#                 answer +=1
#             elif index ==0:
#                 if name[index-1] != "A":
#                     index -=1
#                     answer+=1
#                 elif name[index+1] != "A":
#                     index +=1
#                     answer+=1
#                 elif name[index+1] == "A" and name[index-1] == "A":
#                     index -=1
#                     answer +=1
                    
#             elif index >0:
#                 index+=1
#                 answer+=1
#             cursor_count +=1
#         elif ord(name[index]) == 65:
#             if index < 0 :
#                 index -=1
#                 answer +=1
#             elif index ==0:
#                 if name[index-1] != "A":
#                     index -=1
#                     answer+=1
#                 elif name[index+1] != "A":
#                     index +=1
#                     answer+=1
#                 elif name[index+1] == "A" and name[index-1] == "A":
#                     index -=1
#                     answer +=1
#             elif index >0:
#                 index+=1
#                 answer+=1
            
#         else:
#             answer += ord(name[index])- 65
#             if index < 0 :
#                 index -=1
#                 answer +=1
#             elif index ==0:
#                 if name[index-1] != "A":
#                     index -=1
#                     answer+=1
#                 elif name[index+1] != "A":
#                     index +=1
#                     answer+=1
#                 elif name[index+1] == "A" and name[index-1] == "A":
#                     index -=1
#                     answer +=1
#             elif index >0:
#                 index+=1
#                 answer+=1
#             cursor_count +=1
#     return answer-1