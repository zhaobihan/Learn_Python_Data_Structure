class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    # return the top element, not remove
    def peek(self):
        if not self.is_empty():    # note: call the method using self
            return self.items[-1]

    def get_stack(self):
        return self.items


myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")
print(myStack.peek())