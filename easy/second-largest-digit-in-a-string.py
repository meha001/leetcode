__author__ = 'meha001'

from typing import *

class Solution:
    def secondHighest(self, s: str) -> int:
        t = []
        for i in s:
            if i.isdigit():
                t.append(int(i))
        return sorted(list(set(t)))[::-1][1]