class DListNode :
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def revTraversal(tail):
    curNode = tail
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.prev


# Given the head, tail, and probe references, probe the list for a target.
def probList(head, tail, probe, target):
    # Make sure the list is not empty.
    if head is None:
        return False
    # If probe is null, initialize it to the first node.
    elif probe is None:
        probe = head

    # If the target comes before the probe node, we traverse backward;
    # otherwise traverse forward.
    if target < probe.data:
        while probe is not None and target <= probe.data:
            if target == probe.data:
                return True
            else:
                probe = probe.prev
    else:
        while probe is not None and target >= probe.data:
            if target == probe.data:
                return True
            else:
                probe = probe.next

    # If the target is not found in the list, return False.
    return False

# Given a head and tail reference and a new value, add the new value to a
# sorted doubly linked list.
def addNode(head, tail, value):
    newnode = DListNode(value)
    if head is None: # empty list
        head = newnode
        tail = head
    elif value < head.data: # insert before head
        newnode.next = head
        head.prev = newnode
        head = newnode
    elif value > tail.data: # insert after tail
        newnode.prev = tail
        tail.next = newnode
        tail = newnode
    else: # insert in the middle
        node = head
        while node is not None and node.data < value:
            node = node.next

        newnode.next = node
        newnode.prev = node.prev
        node.prev.next = newnode
        node.prev = newnode