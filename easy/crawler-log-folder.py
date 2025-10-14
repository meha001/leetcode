__author__ = 'meha001'

from typing import *

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        t = []
        for i in logs:
            if '/' in i and '.' not in i:
                t.append(i)
            if i == '../':
                if t: t.pop()
                
        return len(t)