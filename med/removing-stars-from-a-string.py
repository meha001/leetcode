__author__ = 'meha001'

from typing import *

class Solution:
    def removeStars(self, s: str) -> str:
        t = []
        for i in s:
            if i == '*':t.pop()
            else:t.append(i)
        return ''.join(t)