# Write code to remove duplicattes from an unsorted linked list

# Follow up:
# How would you solve this problem if a temporary
# buffer is not allowed?


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        return self.next


class LinkedList():
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def remove_dups(self):
        # ---- SOLUTION ----
        # Algorithm will run in O(N) linear time
        # traversal for list of size N
        nodes_dict = {}
        current = self.head
        previous = None
        while current is not None:
            if current.data not in nodes_dict:
                nodes_dict[current.data] = 1  # append node to hashmap
                previous = current
            else:
                previous.next = current.next
            current = current.next
        return self
