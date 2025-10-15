__author__ = 'meha001'
from typing import *

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        t = list(s)
        print(t)
        t2 = list(goal)
        for i in range(len(t)):
            if t == t2:
                return True
            else:
                s2 = '' + t[0]
                t.pop(0)
                t.append(s2)
        return False