import sys

computer = int(sys.stdin.readline())
link = int(sys.stdin.readline())

graph = {} # 딕셔너리 형태로 저장

for _ in range(link):
    comp1, comp2 = map(int, sys.stdin.readline().split())
    if comp1 not in graph:
        graph[comp1] = set([comp2]) # set함수를 통해 comp1, comp2 저장 시 발생하는 중복값 제거
    if comp2 not in graph:
        graph[comp2] = set([comp1])
    if comp1 in graph:
        graph[comp1].add(comp2)
    if comp2 in graph:
        graph[comp2].add(comp1)  # comp1, comp2의 연결을 모두 반영하는 딕셔너리 만듬(value값은 set 함수 형태)
 
stack = [1] # 1번 컴퓨터가 문제의 기준이 되므로 stack에 미리 넣어줌
visited = []

while stack:
    v = stack.pop() 
    if v not in visited:
        visited.append(v)
    else:
        continue # visited 리스트에 있을 시 아래 과정 생략(continue)

    temp = list(graph[v]) # value값이 set함수 형태이므로 임시 변수에 넣어 리스트로 바꿔줌
    for i in temp:
        stack.append(i) #v 컴퓨터(key)에 연결된 모든 컴퓨터 값(value)을 stack에 넣어줌

print(len(visited)-1) # 처음 기준이 된 1번 컴퓨터를 제외한 visited 리스트 내의 원소의 갯수 출력