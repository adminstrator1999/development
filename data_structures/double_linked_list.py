class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_first(self, value):
        node = Node(value)
        if not self.head:
            self.head.previous = node
            node.next = self.head
        self.head = node
        self.size += 1

    def remove_first(self):
        if not self.head:
            return None
        target = self.head
        self.head = target.next
        self.head.previous = None
        self.size -= 1
        return target.value

    def add_last(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            node.previous = current
            self.size += 1

    def remove_last(self):
        if not self.head:
            return None

        current = self.head
        while current.next is not None:
            current = current.next
        if current.previous is None:
            self.head = None
        else:
            previous = current.previous
            previous.next = None
            current.previous = None
        self.size -= 1
        return current.value

    def remove(self, index):
        if index == 0:
            return self.remove_first()
        target = self.head
        for _ in range(index):
            target = target.next
        previous = target.previous
        if not target.next:
            previous.next = None
        else:
            previous.next = target.next
            target.next.previous = previous
        return target.value

    def contains(self, value):
        pass
