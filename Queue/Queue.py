class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.empty() != True:
            return self.queue.pop(0)
        else:
            return None

    def empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def show(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

    def front(self):
        return self.queue[0]

    def rear(self):
        return self.queue[-1]
