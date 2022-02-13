class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      1
#     / \
#    2   3
#  / \    \
# 4   5    7
