from Queue import Queue


def levelorder(root):
    q = Queue()
    p = root
    while p != None:
        print(p.data, end=" ")
        if p.left:
            q.enqueue(p.left)
        if p.right:
            q.enqueue(p.right)
        p = q.dequeue()
    print("\n")
