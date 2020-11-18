# 4번) 여행경로
# 테스트 1,2 통과 X
def solution(tickets):
    final = ['ICN',]
    while tickets:
        nxt = sorted(route for route in tickets if route[0]==final[-1])[0]
        # filter?
        final.append(nxt[1])
        tickets.remove(nxt)
    return final
