# my own implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def add_last(self, value):
        node = Node(value)
        current = self.head
        if current:
            while current.next is not None:
                current = current.next
            current.next = node
            self.size += 1
        else:
            self.head = node

    def remove_last(self):
        current = self.head
        if current:
            while current.next is not None:
                next = current.next
                if not next.next:
                    current.next = None
                    self.size -= 1
                    return next.value
                current = next

    def add_first(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def remove_first(self):
        if self.head:
            target = self.head
            self.head = target.next
            self.size -= 1
            return target.value

    def remove(self, index):
        if index == 0:
            self.remove_first()
        else:
            current = self.head
            target = current.next
            while index-1 > 0:
                current = current.next
                index -= 1
            current.next = target.next
            self.size -= 1
            return target.value

    def contains(self, value):
        current = self.head
        if current:
            index = 0
            while current.value != value:
                index += 1
                current = current.next
            return index


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class LinkedList:
#
#     def __init__(self):
#         self.root = None
#         self.size = 0
#
#     def add_last(self, value):
#         node = Node(value)
#         if self.root:
#             current = self.root
#             while current.next:
#                 current = current.next
#             current.next = node
#         else:
#             self.root = node
#
#     def remove_last(self):
#         current = self.root
#         if current.next:
#             while current.next:
#                 current = current.next
#             target = current
#             current.next = None
#             return target.value
#         self.root = None
#         return None
#
#     def add_first(self, value):
#         node = Node(value)
#         node.next = self.root
#         self.root = node
#
#     def remove_first(self):
#         first = self.root
#         if first:
#             self.root = first.next
#             return first.value
#
#     def remove(self, index):
#         if index == 0:
#             return self.remove_first()
#         i = 0
#         current = self.root
#         while current:
#             previous = current
#             current = current.next
#             i += 1
#             if i == index:
#                 previous.next = current.next
#                 self.size -= 1
#                 return current.value
#
#     def contains(self, value):
#         if self.root:
#             index = 0
#             current = self.root
#             while current:
#                 if current.value == value:
#                     return index
#                 current = current.next
#                 index += 1
