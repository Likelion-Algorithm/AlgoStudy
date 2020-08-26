n, m = map(int, input().split())

s = []

def f():
  if len(s) == m:
    for i in s:
        print(i, end= ' ')
    print()
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    s.append(i)
    f()
    s.pop()

f()