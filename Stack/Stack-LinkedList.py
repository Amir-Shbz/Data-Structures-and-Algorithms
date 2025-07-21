class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):

        return self.top is None

    def push(self, new_data):

        new_node = Node(new_data)

        if not new_node:
            print("\nStack Overflow")
            return

        new_node.next = self.top
        self.top = new_node

    def pop(self):

        if self.is_empty():
            print("\nStack Underflow")
        else:

            temp = self.top
            self.top = self.top.next
            del temp

    def peek(self):

        if not self.is_empty():
            return self.top.data
        else:
            print("\nStack is empty")
            return float('-inf')