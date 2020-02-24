import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.add_to_tail(value)
        self.size += 1
        return

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.remove_from_tail()

    def len(self):
                return self.size

