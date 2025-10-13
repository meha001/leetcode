__author__ = 'meha001'

from typing import List

class MyQueue:

    def __init__(self):
        self.quere = []

    def push(self, x: int) -> None:
        self.quere.append(x)

    def pop(self) -> int:
        return self.quere.pop(0)

    def peek(self) -> int:
        return self.quere[0]

    def empty(self) -> bool:
        return len(self.quere) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()