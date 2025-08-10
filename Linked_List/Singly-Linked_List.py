class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def showlist(self):
        r = self.head
        while(r != None):
            print(r.data, end=' ')
            r = r.next
        print("\n")

    def insert(self, x, index=-1):
        n = Node(x)
        if self.head == None:
            self.head = n
            return
        elif index == -1:
            r = self.head
            while(r.next != None):
                r = r.next
            newnode = n
            r.next = newnode
        else:
            r = self.head
            q = None
            i = 0
            while(i < index):
                q = r
                r = r.next
                i += 1
            q.next = n
            n.next = r

    def reverse(self):
        t = self.head
        r = self.head
        q = None
        while(r != None):
            t = t.next
            r.next = q
            q = r
            r = t
        self.head = q

    def delete(self, x):
        r = self.head
        q = None
        while(r != None):
            if r.data == x:
                if r == self.head:
                    self.head = r.next
                    r.next = None
                else:
                    q.next = r.next
                    r.next = None
                break
            q = r
            r = r.next

    def getindex(self, x):
        l = -1
        r = self.head
        while(r != None):
            l += 1
            if r.data == x:
                return l
            else:
                r = r.next
        return -1

    def length(self):
        l = 0
        r = self.head
        while(r != None):
            l += 1
            r = r.next
        return l
