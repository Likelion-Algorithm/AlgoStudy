import sys
from collections import deque
node = int(sys.stdin.readline())
graph = dict()
for i in range(node):
    vertex, *rest = sys.stdin.readline().split()
    graph[vertex] = []
    graph[vertex].extend(rest)


def preorder(graph, node, result):
    left, right = graph[node]
    result.append(node)
    if left != ".":
        preorder(graph, left, result)
    if right != ".":
        preorder(graph, right, result)
    return "".join(result)
    # stack = ["A"]
    # result = []
    # while stack:
    #     temp = stack.pop()
    #     result.append(temp)
    #     left, right = graph[temp]
    #     if right != '.':
    #         stack.append(right)
    #     if left != '.':
    #         stack.append(left)
    # return "".join(result)


def inorder(graph, node, result):
    left, right = graph[node]
    if left != ".":
        inorder(graph, left, result)
    result.append(node)
    if right != ".":
        inorder(graph, right, result)
    return "".join(result)
    # while stack:
    #     print(result, stack)
    #     temp = stack.pop()

    #     if temp == "A":
    #         result.append(temp)
    #         left, right = graph[temp]
    #         stack.append(left)
    #         stack.append(right)

    #     else:
    #         for i in \
    #         left, right = graph[temp]
    #         if right != '.':
    #             stack.append(right)
    #             result.insert(result.index(temp)+1, right)
    #         if left != '.':
    #             stack.append(left)
    #             result.insert(result.index(temp), left)
    # return result
    # while deq:
    #     temp = deq.popleft()
    #     left, right = graph[temp]
    #     if left == '.':
    #       result.append(temp)
    #       parent = deq.popleft()
    #     else:
    #       deq.append(left)
    #       deq.append(temp)

    return


def postorder(graph, node, result):
    left, right = graph[node]
    if left != '.':
        postorder(graph, left, result)
    if right != '.':
        postorder(graph, right, result)
    result.append(node)
    return "".join(result)


pre = preorder(graph, "A", [])
print(pre)
ino = inorder(graph, "A", [])
print(ino)
post = postorder(graph, "A", [])
print(post)