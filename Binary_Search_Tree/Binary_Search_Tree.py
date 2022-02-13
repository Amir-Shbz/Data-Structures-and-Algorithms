from Level_Order_Traversal import levelorder


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


class BST():
    def __init__(self):
        self.root = Node(None)

    def insert(self, x):
        if self.root.data == None:
            self.root.data = x
            return

        r = self.root
        n = Node(x)
        q = 0

        while q != -1:
            if r.data > n.data:
                if r.left:
                    r = r.left
                else:
                    q = -1
            else:
                if r.right:
                    r = r.right
                else:
                    q = -1

        if r.data > n.data:
            r.left = n
        else:
            r.right = n

    def show(self):
        r = self.root
        levelorder(r)

    def delete(self, x):
        r = self.root
        q = None

        while r.data != x:
            q = r
            if x > r.data:
                r = r.right
            else:
                r = r.left

        if r.left == None and r.right == None:
            if q.left == r:
                q.left = None
            elif q.right == r:
                q.right = None

        elif r.left == None and r.right != None:
            if q.left == r:
                q.left = r.right
            elif q.right == r:
                q.right = r.right

        elif r.left != None and r.right == None:
            if q.left == r:
                q.left = r.left
            elif q.right == r:
                q.right = r.left

        elif r.left != None and r.right != None:
            q = r
            t = r
            r = r.left
            while r.right:
                t = r
                r = r.right
            t.left = r.left
            q.data = r.data
