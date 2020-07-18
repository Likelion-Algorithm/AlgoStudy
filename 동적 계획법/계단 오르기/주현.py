num = int(input())
stairList = list()
maxList = list()
stairList.append(0)
stairList.append(0)
for i in range(num):
    stairList.append(int(input()))
maxList.append(0)
if num>0:
    maxList = stairList[0:3]
if num>1:
    for i in range(3,num+2):
        maxList.append(maxList[i-3]+stairList[i-1]+stairList[i] if maxList[i-3]+stairList[i-1]+stairList[i]>maxList[i-2]+stairList[i] else maxList[i-2]+stairList[i])
'''핵심이 되는 반복문이다. 10,20,25,15,30이라는 예시가 주어지면 문제의 크기가 4일때의 최대값은
   10+25+15가 큰지, 20+15가 큰지를 비교하는 구문이다. 20에도 적용하기 위해 배열은 0,0,10,20....
   으로 시작한다.'''
print(maxList[-1])

