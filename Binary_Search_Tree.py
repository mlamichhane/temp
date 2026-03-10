class Node:
    def __init__(self, value):
        self.data = value
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.data:
            if node.left_child is None:
                node.left_child = Node(value)
            else:
                self._insert_recursive(node.left_child, value)
        else:
            if node.right_child is None:
                node.right_child = Node(value)
            else:
                self._insert_recursive(node.right_child, value)


def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)

if __name__ == "__main__":

    bst = BinarySearchTree()
    bst.insert(14)
    bst.insert(15)
    bst.insert(4)
    bst.insert(9)
    bst.insert(7)
    bst.insert(18)
    bst.insert(3)
    bst.insert(16)
    bst.insert(20)
    bst.insert(17)
    bst.insert(5)

    print("Inorder Traversal:")
    print("******************")
    inorder(bst.root)