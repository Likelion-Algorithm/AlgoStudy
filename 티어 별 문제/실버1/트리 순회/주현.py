from collections import(deque)
n = int(input())
tree = dict()
for i in range(n):
    x,y,z = input().split()
    tree[x] = [y,z]

def Preorder(node):
    print(node, end='')
    if tree[node][0] != '.':
        Preorder(tree[node][0])
    if tree[node][1] != '.':
        Preorder(tree[node][1])
def Inorder(node):
    if tree[node][0] != '.':
        Inorder(tree[node][0])
    print(node, end='')
    if tree[node][1] != '.':
        Inorder(tree[node][1])
def Postorder(node):
    if tree[node][0] != '.':
        Postorder(tree[node][0])
    if tree[node][1] != '.':
        Postorder(tree[node][1])
    print(node, end='')

Preorder('A')
print()
Inorder('A')
print()
Postorder('A')