def dequeue(queue):           
    queue.append(queue.pop(0))      
#실제 dequeue동작은 첫 원소를 없애는 것만을 뜻하지만 편의상 꼬리에 붙이는 동작을 포함했다.
def reverseDequeue(queue):
    temp = queue.pop()
    queue.insert(0,temp)
#마찬가지로 실제 dequeue와는 반대방향으로 동작한다. 순환큐에서만 가능한 듯 하다.
qsize, num = map(int, input().split())      #문제에서 queue의 크기를 제시해 주는데, 필요할 때가 있나?
locations =list(map(int, input().split()))  #문제의 첫 번째 연산을 목표로하는 원소들의 집합
queue=[]
count=0                            #2,3번째 연산의 수를 세기 위한 변수
for i in range(1, qsize+1):        #n번째 원소의 값을 n으로 하는 순환큐를 생성
    queue.append(i)
for i in locations:
    for j in range(0, len(queue)):
        if(i==queue[j]):
            break
    for k in range(len(queue)-1,-1,-1):
        if(i==queue[k]):
            break
    if(j<(len(queue)-1)-k+1):
        for a in range(0,j):
            dequeue(queue)
            count+=1
        queue.pop(0)
    else:
        for b in range(len(queue)-1,k-1,-1):
            reverseDequeue(queue)
            count+=1
        queue.pop(0)
#2번 연산을 한 후 pop하는 것이 빠른 지, 3번 연산을 하고 pop하는 것이 빠른 지 계산 후 pop한다.
print(count)#출력

'''문제를 정확하게 이해하는 것이 제일 중요한 문제다. 가장 핵심이 되는 힌트는 
문제를 풀기 위해 구현해야 할 동작이 딱 세개라는 것이다. 맨 첫 원소를 pop하는 동작과
왼쪽으로 돌리기, 오른쪽으로 돌리기. 딱 세개다. 이후는 그냥 숫자놀음이 되는데, 문제 가독성이
떨어져서 숫자가 어떻게 돌아가는지 파악하는게 너무힘들었다.'''