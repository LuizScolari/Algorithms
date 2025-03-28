class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addHead(self, value):
        new_node = Node(value)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def addTail(self, value):
        new_node = Node(value)
        new_node.prev = self.tail

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def removeHead(self):
        if not self.head:
            return None
        removed = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return removed

    def removeTail(self):
        if not self.tail:
            return None
        removed = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else: 
            self.head = None
        return removed

class TestDoubleLinkedList:
    def test_operations(self):
        dll = DoubleLinkedList()

        print("\nAdicionando 1 na head:")
        dll.addHead(1)
        print(f"Head: {dll.head.value}, Tail: {dll.tail.value}")

        print("\nAdicionando 2 na tail:")
        dll.addTail(2)
        print(f"Head: {dll.head.value}, Tail: {dll.tail.value}")

        print("\nAdicionando 3 na tail:")
        dll.addTail(3)
        print(f"Head: {dll.head.value}, Tail: {dll.tail.value}")

        print("\nAdicionando 0 na head:")
        dll.addHead(0)
        print(f"Head: {dll.head.value}, Tail: {dll.tail.value}")

        print("\nRemovendo da head:")
        removed = dll.removeHead()
        print(f"Removido: {removed}, Head: {dll.head.value if dll.head else None}, Tail: {dll.tail.value if dll.tail else None}")

        print("\nRemovendo da tail:")
        removed = dll.removeTail()
        print(f"Removido: {removed}, Head: {dll.head.value if dll.head else None}, Tail: {dll.tail.value if dll.tail else None}")

        print("\nRemovendo toda a lista:")
        dll.removeHead()
        dll.removeHead()
        print(f"Head: {dll.head}, Tail: {dll.tail}")

        print("\nTentando remover da head em lista vazia:")
        removed = dll.removeHead()
        print(f"Removido: {removed}")

        print("\nTentando remover da tail em lista vazia:")
        removed = dll.removeTail()
        print(f"Removido: {removed}")

test = TestDoubleLinkedList()
test.test_operations()
