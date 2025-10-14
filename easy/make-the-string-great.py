__author__ = 'meha001'

from typing import *

class Solution:
    def makeGood(self, s: str) -> str:
        if not s:  
            return ""
            
        t = [s[0]]
        for i in range(1, len(s)):
            if t and s[i] == t[-1].swapcase():
                t.pop()
            else:
                t.append(s[i])
        return ''.join(t)