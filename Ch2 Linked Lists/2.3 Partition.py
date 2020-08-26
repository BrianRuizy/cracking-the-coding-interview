# 2.3 Partition
# write code to partition a linkedlist around a vlaue x,such that all nodes
# less than x come before all nodes greater than or equal to x.

# Important:
# the partition element x can appear anywhere in the
# 'right partition' it does not need to appear between the left and right
# partitions. The adddtional spacing the example below indicates the partition

# Example:
# input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 -> Null
# output: 3 -> 1 -> 2    ->    10 -> 5 -> 5 -> 8 -> Null

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __repr__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def partition(self, x):
        """split the linkedlist in two, according to the current node 'n'.
        If (n < x), or (n >= x); respectively

        arguments:
            [node.value]: x
        returns:
            [Node()]: head
        example:
            1->4->3->2->5->2, x = 3
            [1 -> 2 -> 2],[4 -> 3 -> 5]
            1 -> 2 -> 2 -> 4 -> 3 -> 5

        solution would be a 1-pass O(N) traversal of original list,
        where N is the size of the linked-list
        """
        list1 = list1_head = Node()  # will hold nodes < x
        list2 = list2_head = Node()  # will hold nodes >= x

        current = self.head  # pointer to traverse original list
        while current is not None:
            if current.data < x:
                list1.next = current  # add current to list1
                list1 = list1.next  # step
            elif current.data >= x:
                list2.next = current  # add current to list2
                list2 = list2.next  # step
            current = current.next  # step forward in original list

        list1.next = list2_head  # merge the two and return new head
        return list1_head.next.__repr__()
