class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
    
    def set_next(self, new_next):
        self.next = new_next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
    
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count
    
    def search(self, target):
        current = self.head
        while current is not None:
            if current.get_data() == target:
                return True
            current = current.get_next()
        return False
    
    def remove(self, target):
        current = self.head
        previous = None
        while current is not None:
            if current.get_data() == target:
                if previous is None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                return
            previous = current
            current = current.get_next()
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.get_data())
            current = current.get_next()

# Example usage:
if __name__ == "__main__":
    mylist = LinkedList()
    
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    
    mylist.traverse()
    
    mylist.remove(17)
    
    mylist.traverse()
    
    if mylist.search(17):
        print("item found")
    else:
        print("item not found")    