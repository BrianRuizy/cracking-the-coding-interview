# 2.3 Delete Middle Node
# Implement an algorithm to delete a node in the middle.
# (I.e., any node but the first and last node, not the exact middle)
# Given only access to that arg node...
# not the entire list.

# example:
# input: node = c, list = a-> b-> c-> d-> e-> f->Null
# do not return nothing, just modify the linked list a-> b-> d-> e-> f->Null

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            node = Node(data=nodes.pop(0))  # first node, from first data
            self.head = node  # assign head to first node
            for element in nodes:
                node.next = Node(data=element)  # create node object
                node = node.next  # step to next node

    def __repr__(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next
        nodes.append('None')  # signal end of list
        return ' -> '.join(nodes)

    def append_to_tail(self, data):
        # appends new node to tail of list in O(n) linear time
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete_middle_node(self, data):
        # not having acces to list traversel just the current node
        # we can leverage both (node.value, node.next)
        node = Node(data=data)
        if node is None or node.next is None:
            return False

        node.data = node.next.data
        node.next = node.next.next
        return True