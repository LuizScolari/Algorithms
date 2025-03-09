class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not len(self.items):
            raise IndexError("Empty stack")
        
        return self.items.pop()
    
    def peek(self):
        if not len(self.items):
            raise IndexError("Empty stack")
        
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    

stack = Stack()
print("Stack:", stack.items)

stack.push(10)
print(stack.items)

stack.push(20)
print(stack.items)

stack.push(30)
print(stack.items)

top = stack.peek()
print(f"Top: {top}")

size = stack.size()
print(f"Size: {size}")

popped = stack.pop()
print(stack.items)

size = stack.size()
print(f"Size: {size}")

popped = stack.pop()
popped = stack.pop()
print(stack.items)
