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
        # if val x is smaller than the current
        # smallest in min stack, place at top of min stack
        if self.m_stack[-1] > x:
            self.m_stack.append(x)

    def pop(self):
        y = self.stack.pop()  # pop from stack and store as var 'y'
        # if top value is smallest remove it from mins stack
        if self.m_stack[-1] >= y:
            self.m_stack.pop()

    def min(self):
        return self.m_stack[-1]  # return top elem in mins stack
