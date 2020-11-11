def recurse(answer, route,length):
    if not route:
        if answer:
            return answer
    test = []
    for i in range(len(route)):
        if route[i][0] == answer[-1]:
            a = recurse(answer + [route[i][1]], route[:i] + route[i+1:], length)
            if a == None:
                continue
            test.append(a)
    if test:
        return [test[-1], min(test, key=lambda x: ''.join(x))][len(answer) != 1]

def start(tickets):
    answer = []
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            b = recurse([tickets[i][0],tickets[i][1]],tickets[:i]+tickets[i+1:],len(tickets))
            if b:
                answer.append(b)
    return[answer[-1],min(answer,key = lambda x:''.join(x))][len(answer)!=1]



def solution(tickets):
    answer = start(tickets)
    return answer