# TRAVERSING NODES USING A |while| LOOP WITHIN A FUCNTION

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def iter_linked_list(node):
    while node is not None:
        print(node.next)
        node = node.next

head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")
head.next.next.next = Node("4th Node")

iter_linked_list(head)
