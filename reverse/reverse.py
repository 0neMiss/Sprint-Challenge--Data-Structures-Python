class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        #bug is that cur is never hitting none on the while loop, alternates between 4 and 5
        cur = node
        while cur:
            #sets next to the next node
            next = cur.next_node
            #sets prev to tne next node as well
            cur.next_node = prev
            #sets prev to current node
            prev =cur
            #sets cur to next node
            cur =next
        #if cur is none then prev will be head
        self.head = prev
