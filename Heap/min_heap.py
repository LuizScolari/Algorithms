class MinHeap:
    def __init__(self):
        self.heap = []

    def left_child(self, index):
        return 2 * index + 1
    
    def right_child(self, index):
        return 2 * index + 2
    
    def parent(self, index):
        return (index - 1) // 2
    
    def heapify_up(self, index):
        if index == 0:
            return 
        
        parent_index = self.parent(index)
        if self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]  
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        size =len(self.heap)

        left = self.left_child(index)
        right = self.right_child(index)

        smallest = index

        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
    
    def pop_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        if len(self.heap) > 0:
            self.heapify_down(0)

        return root

    def display(self):
        print(self.heap)
    
heap = MinHeap()
heap.insert(3)
heap.insert(1)
heap.insert(6)
heap.insert(5)
heap.insert(2)
heap.insert(4)

heap.display()

while len(heap.heap) > 0:
    print(heap.pop_min())  # (1, 2, 3, 4, 5, 6)