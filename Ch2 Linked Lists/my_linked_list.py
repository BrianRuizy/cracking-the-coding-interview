class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


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

    def append_to_head(self, data):
        # O(1) constant time, as inserting only interacts with head
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

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

    def size(self):
        """traverse list and iterate a counter variable"""
        curr_ptr = self.head
        count = 0
        while curr_ptr is not None:
            count += 1
            curr_ptr = curr_ptr.get_next()
        return count

    def remove_node(self, target):
        """using "Runner" technique"""
        curr_ptr = self.head  # current node pointer
        prev_ptr = None  # previous node pointer
        while curr_ptr is not None:
            if curr_ptr.get_data() == target:
                if prev_ptr:
                    prev_ptr.set_next(curr_ptr.get_next())
                else:
                    self.head = curr_ptr.get_next()
                return True
            prev_ptr = curr_ptr
            curr_ptr = curr_ptr.get_next()
        return False

    def reverse(self):
        """will reverse list iteratively,
        by traversing and flipping the next pointer of each node
        """
        curr_ptr = self.head  # current pointer, at head
        prev_ptr = None  # previous pointer, initialized to null
        while curr_ptr is not None:
            temp = curr_ptr.next  # temp buffer, pointing to next node
            curr_ptr.next = prev_ptr  # reverse link of current_ptr to previous
            prev_ptr = curr_ptr  # resume traversal
            curr_ptr = temp
        self.head = prev_ptr
        return self
