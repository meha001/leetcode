__author__ = 'meha001'

from typing import *

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        t = [start + 2 * i for i in range(n)]
        tl = t[0]
        for i in range(1, len(t)):
            print(tl)
            tl = tl ^ t[i]
            
        return tl[0]