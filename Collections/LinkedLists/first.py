class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def traverse(self):
        node = self
        while node:
            print(node.value)
            node = node.next

node1 = Node(12)
node2 = Node(99)
node3 = Node(37)

node1.next = node2
node2.next = node3

node1.traverse()