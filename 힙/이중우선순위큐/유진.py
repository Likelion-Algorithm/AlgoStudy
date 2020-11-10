# 3번) 
def solution(operations):
    q = []
    for op in operations:
        if 'I' in op:
            num = int(op.split(' ')[1])
            q.append(num)
        elif len(q)!=0:
            if op=='D -1': q.remove(min(q))
            elif op=='D 1': q.remove(max(q))
    if len(q)==0: return [0,0]
    else: return [max(q), min(q)]
