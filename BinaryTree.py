class BinaryTree:
    def __init__(self, obj):
        self.data = obj
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, node_data):
        if self.left_child == None:
            self.left_child = BinaryTree(node_data)
        else:
            temp_node = BinaryTree(node_data)
            temp_node.left_child = self.left_child
            self.left_child = temp_node
    
    def insert_right(self, node_data):
        if self.right_child == None:
            self.right_child = BinaryTree(node_data)
        else:
            temp_node = BinaryTree(node_data)
            temp_node.right_child = self.right_child
            self.right_child = temp_node
    
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)

def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)

def postorder( root_node):
    current = root_node
    if current is None:
        return
    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data)

if __name__ == "__main__":
    r = BinaryTree('a')
    # print(r.get_data()) 
    # print(r.get_left_child())
    r.insert_left('b')
    # print(r.get_left_child())
    # print(r.get_left_child().get_data())
    r.insert_right('c') 
    # print(r.get_right_child()) 
    # print(r.get_right_child().get_data()) 
    # r.get_right_child().set_data('hello') 
    # print(r.get_right_child().get_data())

    print("In-order Traversal")
    inorder(r)
    print("-------------")
    print("Pre-order Traversal")
    preorder(r)
    print("-------------")
    print("Post-order Traversal")
    postorder(r)
    print("-------------")

    

