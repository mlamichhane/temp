class ListNode :
    def __init__(self, data):
        self.data = data
        self.next = None

def traversList(head):
    currentNode = head
    while currentNode:
        print(currentNode.data)
        currentNode = currentNode.next

def searchList(head, target):
    currentNode = head
    while currentNode is not None and currentNode.data != target:
        currentNode= currentNode.next
    return currentNode is not None

# Given the head reference, remove a target from a linked list.
def removeNode(head, target):
    predNode = None
    curNode = head
    while curNode is not None and curNode.data != target:
        predNode = curNode
        curNode = curNode.next

    if curNode is not None:
        if curNode is head:
            head = curNode.next
        else :
            predNode.next = curNode.next


if __name__ == "__main__":
    a = ListNode(11)
    b = ListNode(52)
    c = ListNode(18)

    a.next = b
    b.next = c

    # print(a.data)
    # print(a.next.data)
    # print(a.next.next.data)

    # Given the head pointer, prepend an item to an unsorted linked list.
    newNode = ListNode(100)
    newNode.next = a
    a = newNode
    
    

    traversList(a)

    removeNode(a, 52)

    traversList(a)
    # if searchList(a, 45):
    #     print("item found")
    # else:
    #     print("item not found")


