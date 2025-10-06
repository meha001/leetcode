__author__ = 'meha001'

from typing import *

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
            
        min_a = m
        min_b = n
        
        for op in ops:
            min_a = min(min_a, op[0])
            min_b = min(min_b, op[1])
        
        return min_a * min_b

print(Solution().maxCount(3, 3, [[2, 2], [3, 3]])) 