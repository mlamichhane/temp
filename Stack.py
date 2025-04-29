class Stack:
    def __init__(self, capacity):
        self.stack = [None] * capacity  # Pre-allocate space
        self.capacity = capacity
        self.top = -1                   # Stack is empty initially

    def push(self, item):
        if self.top == self.capacity - 1:
            print("Stack Overflow! Cannot push.")
            return
        self.top += 1
        self.stack[self.top] = item
        #print(f"Pushed {item} --> Stack: {self.stack[:self.top+1]}")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop.")
            return None
        item = self.stack[self.top]
        self.stack[self.top] = None  # Optional: clear the slot
        self.top -= 1
        #print(f"Popped {item} --> Stack: {self.stack[:self.top+1]}")
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

# Example usage
if __name__ == "__main__":
    s = Stack(3)
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)  # Should give overflow
    print(f"Top element: {s.peek()}")
    s.pop()
    print(f"Stack size: {s.size()}")
    s.pop()
    s.pop()
    s.pop()  # Should give underflow
