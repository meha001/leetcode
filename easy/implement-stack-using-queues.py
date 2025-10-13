__author__ = 'meha001'

from typing import List

class MyStack:

    def __init__(self):
        self.quere = []

    def push(self, x: int) -> None:
        self.quere.append(x)

    def pop(self) -> int:
        s = 0
        s += self.quere[-1]
        self.quere.pop()
        return s

    def top(self) -> int:
        return self.quere[-1]

    def empty(self) -> bool:
        return len(self.quere) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()