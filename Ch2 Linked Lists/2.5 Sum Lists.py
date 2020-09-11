# YOu have two numbers represeneted by a linked list, weher aech node conains a single digit. 
# The digits are stored in reverse order, such that the 1's digit is at the head of the list.
# Write a funciton that adds the two numbers and returns the suma s a linked list. 
# Note:
# You are not allowed to 'cheat' and just convert the linked list to an integer

# Example:
# input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# output: 2 -> 1 -> 9. That is 912.

# Follow up:
# - suppose the digits are stored in forward order. Repeat the above problem. 

# Example:
# input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295
# output: 9 -> 1 -> 2. That is, 912.


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            # buffer pointer
            current = Node(data=nodes.pop(0))
            self.head = current
            for x in nodes:  # if more than one data
                current.next = Node(data=x)
                current = current.next

    def __repr__(self):
        # traverse and copy node value to list
        # return dev-friendly string representation of list
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def sum_lists(self):
        # traverse first list
        # variable sum
        # total = Σi=0 = a x 10^0 + a x 10^1 + a x 10^2  ...a x 10^n
        total, exponent = 0, 0
        current = self.head
        while current is not None: 
            total += current.data * (10 ** exponent)
            exponent += 1
            current = current.next
        return total
