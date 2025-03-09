class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("Empty stack")
        
        pop_node = self.top
        self.top = pop_node.next
        self._size -= 1

        return pop_node.value
    
    def peek(self):
        if self.top is None:
            raise IndexError("Empty stack")
        
        return self.top.value
    
    def size(self):
        return self._size
    
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  # 30
print(stack.pop())  # 20
print(stack.pop())  # 10

try:
    stack.pop()  # Error
except IndexError:
    print("Error: empty stack")