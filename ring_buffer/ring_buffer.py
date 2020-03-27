from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        elif not self.current:
            self.storage.head.value = item
            self.current = 1
        else:
            ptr = self.storage.head
            for i in range(self.current):
                ptr = ptr.next
            ptr.value = item
            self.current += 1
            if self.current == self.capacity:
                self.current = 0

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        ptr = self.storage.head
        while ptr is not None:
            if ptr.value is not None:
                list_buffer_contents.append(ptr.value)
            ptr = ptr.next
        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.length = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        return [i for i in self.storage if i is not None]
