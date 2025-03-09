class MinStack:

    def __init__(self):
        self.items = []
        self.min = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if self.min:
            if val <= self.min[-1]:
                self.min.append(val)
        else:
            self.min.append(val)

    def pop(self) -> None:
        if self.items[-1] == self.min[-1]:
            self.min.pop()
        self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        if self.min:
            return self.min[-1]
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()