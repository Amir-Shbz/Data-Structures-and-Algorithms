class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def append_right(self, value):
        if self.is_full():
            raise IndexError("Deque is full")
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.data[self.front] = value
        self.size += 1

    def append_left(self, value):  
        if self.is_full():
            raise IndexError("Deque is full")
        r = (self.front + self.size) % self.capacity
        self.data[r] = value
        self.size += 1

    def pop_right(self):            
        if self.size == 0:
            return None
        res = self.l[self.front]
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return res
    
    def pop_left(self):             
        if self.size == 0:
            return None
        rear = (self.front + self.size - 1) % self.cap
        self.size -= 1
        return self.l[rear]

    def is_empty(self):             
        return self.size == 0 

    def is_full(self):
        return self.size == self.capacity             