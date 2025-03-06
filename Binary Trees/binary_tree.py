class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_recursive(data, self.root)

    def insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else: 
                self.insert_recursive(data, node.right)
    
    def search(self, data):
        return self.search_recursive(self.root, data)
    
    def search_recursive(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        if data < node.data:
            return self.search_recursive(node.left, data)
        else:
            return self.search_recursive(node.right, data)
        
    def preorder_transversal(self):
        result = []
        self.preorder_recursive(self.root, result)
        return result
    
    def preorder_recursive(self, node, result):
        if node:
            result.append(node.data)
            self.preorder_recursive(node.left, result)
            self.preorder_recursive(node.right, result)

    def inorder_transversal(self):
        result = []
        self.inorder_recursive(self.root, result)
        return result
    
    def inorder_recursive(self, node, result):
        if node:
            self.inorder_recursive(node.left, result)
            result.append(node.data)
            self.inorder_recursive(node.right, result)
    
    def postorder_transversal(self):
        result = []
        self.postorder_recursive(self.root, result)
        return result
    
    def postorder_recursive(self, node, result):
        if node:
            self.postorder_recursive(node.left, result)
            self.postorder_recursive(node.right, result)
            result.append(node.data)

tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(2)
tree.insert(8)
tree.insert(1)
tree.insert(10)

print(tree.search(5))
print(tree.search(3))
print(tree.search(2))
print(tree.search(8))
print(tree.search(1))
print(tree.search(10))
print(tree.search(7))

print(tree.preorder_transversal())
print(tree.inorder_transversal())
print(tree.postorder_transversal())