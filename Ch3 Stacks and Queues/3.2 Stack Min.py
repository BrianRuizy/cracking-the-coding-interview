# How would ou design a stack wich in dation to push and pop,
# has a function min which returns the minimum element?
# Push, pop and in should all operate in O(1) time.


# use 2 stacks, to keep track of min value
import sys


class StackMin:
    def __init__(self):
        self.stack = []
        self.m_stack = [sys.maxsize]  # stack to keep track of minimum values

    def __repr__(self):
        return ','.join(str(val) for val in [self.stack])

    def push(self, x):
        self.stack.append(x)
        if self.m_stack[-1] > x:
            self.m_stack.append(x)

    def pop(self):
        y = self.stack.pop()
        if self.m_stack[-1] >= y:
            self.m_stack.pop()

    def min(self):
        return self.m_stack[-1]
