class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(head):
    # a->b->c->None
    # c->b->a->None
    current = head
    previous = None
    while True:
        # b | c | None
        temp_current = current.next
        # a -> None | b->a | c->b
        current.next = previous
        # a|b|c
        previous = current
        if not temp_current:
            break
        # b | c
        current = temp_current

    return current

node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
a = reverse_linked_list(node)
b= a