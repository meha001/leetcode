__author = 'meha001'

from typing import List

class Solution:
    def minimumSum(self, num: int) -> int:
        t = list(str(num))
        a1 = min(t)
        t.remove(min(t))
        b1 = min(t)
        t.remove(min(t))
        a2 = min(t)
        t.remove(min(t))
        b2 = min(t)
        t.remove(min(t))
        
        return int(a1 + b1) + int(a2 + b2)