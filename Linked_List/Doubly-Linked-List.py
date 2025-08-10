class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def forward_traversal(self):
        x = self.head
        while x != None:
            print(x.data)
            x = x.next

    def backward_traversal(self):
        x = self.tail
        while x != None:
            print(x.data)
            x = x.prev

    def findSize(self):
        x = self.head
        l = 0
        while x != None:
            l += 1
            x = x.next

        return l    
    
    def insert_at_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

        if self.findSize() == 1:
            self.tail = new_node

    def insert_end(self, new_data): 
        new_node = Node(new_data)
        self.tail.next = new_node
        if self.tail is not None:
            new_node.prev = self.tail  
        self.tail = new_node 

    def insert_at_position(self, pos, new_data):        
        if pos == 1:
            self.insert_at_front(new_data)
        elif pos == self.findSize()+1:
            self.insert_end(new_data)
        else:
            new_node = Node(new_data)
            p = 1
            point = self.head
            while p < pos:
                point = point.next
                p += 1

            point1 = point.next
            point.next = new_node
            new_node.prev = point

            new_node.next = point1
            point1.prev = new_node    