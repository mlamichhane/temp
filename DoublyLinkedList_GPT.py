class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        """Add a node to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        """Delete the first occurrence of a node with given data."""
        current = self.head
        while current:
            if current.data == data:
                # Node is the head
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                return
            current = current.next

    def display_forward(self):
        """Display the list in forward direction."""
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def display_backward(self):
        """Display the list in reverse direction."""
        current = self.head
        if not current:
            return
        # Go to the last node
        while current.next:
            current = current.next
        # Traverse backward
        while current:
            print(current.data, end=' ')
            current = current.prev
        print()


## Example Usages
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)
dll.display_forward()   # Output: 5 10 20
dll.display_backward()  # Output: 20 10 5
dll.delete(10)
dll.display_forward()   # Output: 5 20