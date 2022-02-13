# Implementation using list
class Stack:
    def __init__(self):
        self.stack = []

    # push(x)
    def push(self, x):
        self.stack.append(x)

    # pop()
    def pop(self):
        return self.stack.pop()

    # show()
    def show(self):
        print(self.stack)

    # size()
    def size(self):
        return len(self.stack)

    # empty()
    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    # top()
    def top(self):
        return self.stack[-1]
