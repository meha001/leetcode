__author__ = 'meha001'

from typing import *

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for i in s:
            if i == '#':
                if stack: stack.pop()
            if i != '#':
                stack.append(i)
        
        stack2 = []
        for i in t:
            if i == '#':
                if stack2: stack2.pop()
            if i != '#':
                stack2.append(i)
        return stack2 == stack
    