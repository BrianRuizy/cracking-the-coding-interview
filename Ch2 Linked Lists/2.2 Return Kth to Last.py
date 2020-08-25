# implement an algorithm to find the 'k'th to last element
# of a singly linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
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

    def size(self):
        # traverse list iteratively to find length
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def kth_to_last_naive(self, k):
        """ Naive solution method assumes we know,
        or allowed to find the size of the list"""
        counter = 0
        index = self.size() - k
        current = self.head
        while current.next is not None:
            if counter == index:
                return current.data
            counter += 1
            current = current.next

    def kth_to_last(self, k):
        ptr_1 = ptr_2 = self.head  # dual variable assignment
        # make the ptr_1 'k' elements away from ptr_2
        # whenever ptr_1 reaches the end, we will have the kth_to_last on ptr_2
        for _ in range(k):
            if ptr_1 is None:  # meaning out of bounds 'k'
                raise IndexError(f'input k:{k} out of range')
            ptr_1 = ptr_1.next

        while ptr_1 is not None:
            ptr_1, ptr_2 = ptr_1.next, ptr_2.next  # tuple unpacking
        return ptr_2.data
