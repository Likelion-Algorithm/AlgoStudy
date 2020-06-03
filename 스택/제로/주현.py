num = int(input())
stack=list()
zero=0                      #0이 나온 횟수를 저장하는 변수
total=0                     #0의 개수만큼 원소를 지우고 남은 총합을 저장
for i in range(0,num):
    stack.append(int(input()))  #스택생성(리스트)
while stack:                
    if stack[-1]!=0:            #가장 최근의 원소의 0여부 확인
        if zero>0:              #zero를 발견했을 때 최신 원소 삭제
            stack.pop()
            zero-=1
        else:                   #최근의 원소가 0일 때 zero를 1증가
            total+=stack.pop()
    else:
        stack.pop()
        zero+=1
print(total)